import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import types
import urllib
import urllib2
import urlparse
import xml.etree.ElementTree as ET

from optparse import OptionParser
from xml.sax.saxutils import escape

from lib.config import Config
from lib.logger import Logger
from lib.utils import Utils

class Test(object):
    """
    This class represents a test.
    """

    def __init__(self, test_dir, test_name, test_type, test_config,
                 test_logger, test_options, test_args):
        """
        Initializes a test.

        @type test_dir: string
        @param test_dir: The directory of the test.
        @type test_name: string
        @param test_name: The name of the test.
        @type test_type: string
        @param test_type: The type of the test.
        @type test_config: Config
        @param
