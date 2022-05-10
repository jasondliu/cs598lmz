import mmap
import os
import re
import subprocess
import sys
import tempfile

from . import _util

def _get_git_version():
    """
    Return the git version as a tuple of three integers.
    """
    try:
        git_version = subprocess.check_output(['git', '--version'])
    except OSError:
        return None
    match = re.match(r'git version (\d+)\.(\d+)\.(\d+)', git_version)
    if not match:
        return None
    return tuple(int(x) for x in match.groups())

def _get_git_root():
    """
    Return the root of the git repository.
    """
    try:
        git_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
    except OSError:
        return None
    return git_root.strip()

def _get_git_config(key):
    """
    Return the value of the given git config key.
