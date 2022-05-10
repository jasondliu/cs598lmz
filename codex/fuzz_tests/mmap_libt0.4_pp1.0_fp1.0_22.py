import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from collections import defaultdict
from glob import glob
from multiprocessing import Pool
from os.path import basename, dirname, join, exists, isdir, isfile, realpath, splitext
from urllib.parse import urlparse

import requests
import yaml

from . import __version__
from . import utils
from . import config
from . import log
from . import pkg
from . import pkgbuild
from . import repo
from . import sources
from . import __main__ as main
from . import __version__ as version
from . import __name__ as name
from . import __license__ as license
from . import __url__ as url
from . import __author__ as author
from . import __email__ as email
from . import __description__ as description


def get_arch():
    """Get the current architecture."""
    return subprocess.check_output(["uname", "-m"]).decode().strip()


def get_arch_
