import mmap
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import time
import urllib
import urllib2
import urlparse
import zipfile

from distutils.version import LooseVersion

from . import config
from . import utils
from . import exceptions
from . import log
from . import path
from . import process
from . import download
from . import temp
from . import fs
from . import shell
from . import zip
from . import tar
from . import rar
from . import sevenz
from . import gzip
from . import bzip2
from . import xz
from . import lzma

#------------------------------------------------------------------------------
def extract_archive(archive, dest_dir, extract_dir=None, progress_cb=None,
                    overwrite=False, retries=None, retry_delay=None,
                    cleanup=False, checksum=None, checksum_algorithm=None):
    """
    Extracts an archive to a destination directory.

    :param archive: Path to the archive file.
    :param dest_dir: Destination
