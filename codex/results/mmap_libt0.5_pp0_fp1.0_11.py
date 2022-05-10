import mmap
import os
import re
import sys
import time
import traceback

from optparse import OptionParser

from mako.lookup import TemplateLookup
from mako import exceptions

from lib import log
from lib import database
from lib import config
from lib import utils

import web

from web.contrib.template import render_mako

from lib.web import form, utils as webutils

from lib.model import *

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config_file",
            help="Config file", metavar="FILE")
    parser.add_option("-l", "--log", dest="log_file",
            help="Log file", metavar="FILE")
    parser.add_option("-L", "--log-level", dest="log_level",
            help="Log level", metavar="LEVEL")
    parser.add_option("
