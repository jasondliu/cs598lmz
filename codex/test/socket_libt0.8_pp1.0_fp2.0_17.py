import socket

class Logger:
    def __init__(self, level = logging.DEBUG):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    def write(self, message, level = logging.DEBUG):
        self.log_to_console(message, level)
        self.log_to_file(message, level)

    def log_to_console(self, message, level):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)
        self.logger.log(level, message)
        self.logger.removeHandler(console_handler)

