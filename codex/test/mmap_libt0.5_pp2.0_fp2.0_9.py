import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib

from contextlib import contextmanager
from datetime import datetime
from distutils.version import LooseVersion
from optparse import OptionParser
from subprocess import Popen, PIPE, STDOUT

from . import __version__
from . import config
from . import constants
from . import util
from . import metadata
from . import xcode
from . import xcpretty
from . import simctl
from . import xcscheme
from . import exceptions
from . import xcresult
from . import xctest


def run(args=None, env=None, cwd=None):
    if args is None:
        args = sys.argv[1:]

    # Parse options
