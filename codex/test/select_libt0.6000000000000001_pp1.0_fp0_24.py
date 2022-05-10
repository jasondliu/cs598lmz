import select
import time
import sys
import os
import datetime

# path = os.path.dirname(__file__)
# sys.path.append(path + '/../')
# sys.path.append(path + '/../../')
# sys.path.append(path + '/../../../')

from common import utils
from common import errors
from core.conf import conf
from core.conf import logger
from core.server import server
from core.client import client

from common.utils import is_valid_ip
from common.utils import is_valid_port


class Control(object):
    """docstring for Control"""

    def __init__(self, arg):
        super(Control, self).__init__()
        self.arg = arg

    def start(self):
        """
        启动服务
        """
