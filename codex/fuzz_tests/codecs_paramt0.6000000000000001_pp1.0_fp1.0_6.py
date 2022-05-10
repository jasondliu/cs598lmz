import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Compatability with Python 2.6
try:
    import json
except ImportError:
    import simplejson as json

import logging
import random
import unittest

import appscale_logging
from flexmock import flexmock
from .. import appscale_info
from ..appscale_info import AppScaleInfo
from ..local_state import LocalState
from ..tools.appscale_tools import AppScaleTools
from ..tools.parse_args import ParseArgs
from ..tools.appscale_logger import AppScaleLogger
from ..db_interface import DBInterface


class TestAppScaleInfo(unittest.TestCase):


  def test_constructor(self):
    options = flexmock(verbose=True)
    flexmock(ParseArgs)
    ParseArgs.should_receive('parse_args').and_return(options)
    flexmock(LocalState)
    LocalState.should_receive('ensure_appscale_is_running').and_return()
    flexmock(
