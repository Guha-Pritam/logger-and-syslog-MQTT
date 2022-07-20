import logging
import time
from logging.handlers import TimedRotatingFileHandler
import socket
import json


class TenXerLogger:
    def __init__(self, log_file_name):
        self.logger = logging.getLogger()
        self.filename = log_file_name
        logging.basicConfig(filename=self.filename, format='%(levelname)s : %(message)s', filemode='w')
        self.logger.setLevel(logging.DEBUG)
        self.hostname = socket.gethostname()
        self.timestamp = time.time()
        self.handler = TimedRotatingFileHandler(filename=self.filename, when='M', interval=2, backupCount=12)

    def log_core_message(self, message):
        logging.info({"timestamp": self.timestamp, "hostname": self.hostname, "message": message})

    def log_analytics(self, message):
        message['tag'] = 'analytics'
        logging.info({
            "timestamp": self.timestamp,
            "hostname": self.hostname,
            "message": message
        })

    def log_debug_prints(self, message):
        logging.debug({"timestamp": self.timestamp, "hostname": self.hostname, "message": message})

    def log_minor_issues(self, message):
        logging.warning({"timestamp": self.timestamp, "hostname": self.hostname, "message": message})

    def log_error(self, message):
        logging.error({"timestamp": self.timestamp, "hostname": self.hostname, "message": message})


if __name__ == "__main__":
    stu = TenXerLogger('log_file_name')
    stu.log_core_message('this is for INFO')
    stu.log_analytics({
        "Name": "Ubuntu",
        "Version": "17.10",
        "Install": "apt",
        "Owner": "Canonical",
        "Kernel": "4.13"
    })
    stu.log_debug_prints('this is for DEBUG')
    stu.log_minor_issues('this is for WARNING')
    stu.log_error('this is for ERROR')
