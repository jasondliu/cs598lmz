import mmap
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import traceback

from collections import namedtuple
from contextlib import contextmanager
from contextlib import closing

from contextlib2 import ExitStack

from pyp2rpm import settings
from pyp2rpm import utils
from pyp2rpm import exceptions

from pyp2rpm.logger import logger

_pypi = 'https://pypi.python.org/simple/'
_package_index = (
    'https://raw.githubusercontent.com/pypa/pypi-legacy/master/legacy.json'
)

_package_dir = os.path.dirname(os.path.abspath(__file__))
_dist_dir = os.path.join(_package_dir, '..', '..', 'dist')

# TODO: make this configurable
_fedora_release = 'f21'

_python_rpms = {
    'python-argparse': 'python-argparse',
    'python-as
