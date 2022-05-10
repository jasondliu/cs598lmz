import codecs
codecs.register(robot_decoder)
import robot.errors
from robot.parsing import TestData

from robot.running import TestSuite, TestCase
from robot.running import TestSuiteBuilder
from robot.utils import OrderedDict

import types
from wrapper import TestCollector, TestRunner


# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

# globals
ROBOT_VERSION = "2.5"
ROBOT_DIR_NAME = "robot"
ROBOT_LIB_DIR_NAME = "lib"
ROBOT_RESOURCE_DIR_NAME = "resource"
ROBOT_OUTPUT_DIR_NAME = "output"
ROBOT_REPORT_DIR_NAME = "report"
ROBOT_LOG_DIR_NAME = "log"
ROBOT_LINK_REPORT_FILE_NAME = "
