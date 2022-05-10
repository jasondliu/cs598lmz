import mmap
import os
import random
import sys
import tempfile
import time
import traceback
import uuid
import yaml
import pprint

import boto3
import click
import docker
import dockerpty
import docker.errors
import docker.tls
import six
import yaml
import whichcraft

from . import __version__
from . import aws
from . import context
from . import dockerpty
from . import errors
from . import fileutils
from . import parseutils
from . import shell
from . import stats
from . import utils
from . import vcs
from . import host
from . import process
from . import constants
from . import __version__
from . import tty
from . import docker_utils

# This is a much slower alternative to using lsblk.
# It is used because it's compatible with many more distros.
# It takes about 400ms on my machine (i7).
def _df_list(mountpoint):
    cmd = ['df', mountpoint]
    try:
        output = subprocess.check_output(cmd)
    except subprocess
