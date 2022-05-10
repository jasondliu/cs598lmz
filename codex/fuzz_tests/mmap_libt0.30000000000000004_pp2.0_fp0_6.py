import mmap
import os
import sys
import time
import traceback

from . import config
from . import constants
from . import exceptions
from . import logger
from . import utils
from . import version
from . import xlogging

_logger = logger.Logger(__name__)

_logger.start()

_logger.info('Version : {}'.format(version.get_version()))
_logger.info('PID : {}'.format(os.getpid()))
_logger.info('Python : {}'.format(sys.version))
_logger.info('Platform : {}'.format(sys.platform))
_logger.info('Architecture : {}'.format(platform.architecture()))
_logger.info('Machine : {}'.format(platform.machine()))
_logger.info('Processor : {}'.format(platform.processor()))
_logger.info('Node : {}'.format(platform.node()))
_logger.info('System : {}'.format(platform.system()))
_logger.info('Release : {}
