import select
import logging
import sys
import os
import time

# TODO:
# - test with a real serial port and a real device
# - test with a real serial port and a fake device
# - test with a fake serial port and a fake device
# - test with a fake serial port and a real device
# - test with a real serial port and a real device, but with
#   a real device that doesn't respond
# - test with a real serial port and a real device, but with
#   a real device that responds in an unexpected way

class TestSerial(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger('TestSerial')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
        self.logger.info('setUp')

    def tearDown(self):
        self.logger.info('tearDown')
        self.logger.removeHandler(self.logger.handlers[0])

