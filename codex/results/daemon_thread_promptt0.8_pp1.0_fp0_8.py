import threading
# Test threading daemon
from ipsniffer.utils import *
from ipsniffer.service import *
from ipsniffer.logger import *
from ipsniffer.config import Config
parse_args()
logger = Logger(__name__)


def setup_module(module):
    logger.info("setup_module      module:%s", module.__name__)


def teardown_module(module):
    logger.info("teardown_module   module:%s", module.__name__)
    logger.remove_handlers()


def setup_function(function):
    logger.info("setup_function    function:%s", function.__name__)


def teardown_function(function):
    logger.info("teardown_function function:%s", function.__name__)


def test_thread():
    service_configs = {
        'test': {
            'test1': {
                'name': 'test1',
                'command': 'sleep 10'
            },
            'test2': {
                '
