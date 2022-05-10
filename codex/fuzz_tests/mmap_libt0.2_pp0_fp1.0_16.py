import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

from . import config
from . import constants
from . import errors
from . import utils
from . import version

# TODO(dborowitz): Move this to a common location.
def _get_git_version():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
    except subprocess.CalledProcessError:
        return 'unknown'


def _get_version_string():
    return '%s (git: %s)' % (version.VERSION, _get_git_version())


def _get_version_info():
    return {
        'version': version.VERSION,
        'git_version': _get_git_version(),
    }


def _get_build_info():
    return {
        'build_date': constants.BUILD_DATE,
        'build_user': constants.BUILD_USER,
        'build_host': constants.BUILD
