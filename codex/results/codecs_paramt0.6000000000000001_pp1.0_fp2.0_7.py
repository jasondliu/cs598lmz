import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import re
import sys
import subprocess

from . import util

_default_eol = {
    'win32': '\r\n',
    'cygwin': '\r\n',
    'linux': '\n',
    'linux2': '\n',
    'darwin': '\n',
    'java': '\n',
}[_platform]

def _get_eol(path):
    """Get the line endings of a file.

    The file is opened in binary mode to avoid Python's universal newline
    handling.
    """
    with open(path, 'rb') as f:
        data = f.read()
    if b'\r\n' in data:
        return '\r\n'
    elif b'\n' in data:
        return '\n'
    else:
        return _default_eol

def _get_encoding(path):
    """Get the encoding of a file.

    The file is opened in binary
