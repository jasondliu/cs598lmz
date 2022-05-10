from lzma import LZMADecompressor
LZMADecompressor.__module__ = 'lzma'

from sys import version_info
if version_info[0] == 2:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen

if version_info[0] == 2:
    from urllib2 import HTTPError
else:
    from urllib.error import HTTPError

import os
import tempfile
import shutil
import logging
import json
import glob
import zipfile

from . import utils
from . import config
from . import exceptions

logger = logging.getLogger(__name__)

def download_file(url, file_name=None, force=False, check_integrity=True):
    """
    Download a file from a url.

    Parameters
    ----------
    url : str
        The url of the file to download.
    file_name : str, optional
        The filename to save the file as. If None, the filename will be
        extracted from the url.
    force : bool, optional
        Force download even if the file already exists
