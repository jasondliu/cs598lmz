import mmap
import os
import os.path
import re
import subprocess
import sys
import time
import traceback
import urllib

from datetime import datetime
from optparse import OptionParser

from common import *

def get_options():
    parser = OptionParser()

    parser.add_option("--build-dir", dest="build_dir",
                      help="Path to the build directory")
    parser.add_option("--build-number", dest="build_number",
                      help="Build number")
    parser.add_option("--build-type", dest="build_type",
                      help="Build type (debug or release)")
    parser.add_option("--build-arch", dest="build_arch",
                      help="Build architecture (x86 or x86_64)")
    parser.add_option("--test-name", dest="test_name",
                      help="Test name")
    parser.add_option("--test-arch", dest="test_arch",
                      help="Test architecture (x86 or x86_64)")
    parser.add_option("
