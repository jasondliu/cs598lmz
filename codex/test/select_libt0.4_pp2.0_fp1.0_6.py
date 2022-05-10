import select
import sys
import time

from . import utils
from . import config
from . import logger

class Pinger(object):
    def __init__(self, host, timeout=3, count=3):
        self.host = host
        self.timeout = timeout
        self.count = count

    def ping(self):
        logger.info('Pinging {}'.format(self.host))
        cmd = ['ping', '-c', str(self.count), '-W', str(self.timeout), self.host]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.wait()
        return proc.returncode == 0

