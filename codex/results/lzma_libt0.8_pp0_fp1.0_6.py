import lzma
lzma.open = lzma.LZMAFile

import json
import os
import requests
import re
import sqlite3
import sys
import tarfile
import tempfile
import urllib2
import webbrowser

from . import github
from . import run
from . import shell
from .base import *


__all__ = ['Installer', 'install']


def tar_extract(src, dest):
    """
    Extract tar file at `src` to `dest` directory.

    Missing parent directories of `dest` are created if necessary.

    """
    if not os.path.exists(dest):
        os.makedirs(dest)
    with tarfile.open(src) as f:
        f.extractall(dest)


def extract_archive(src, dest):
    """
    Extract archive at `src` to `dest` directory.

    Formats supported are .zip and .tar.gz.

    Missing parent directories of `dest` are created if necessary.

    """
    if os.path.splitext(src)[1] == '.
