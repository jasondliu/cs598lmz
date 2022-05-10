import lzma
lzma.LZMAError
import os
import sys
import tarfile
import tempfile
import time

from . import _util


def _unpack_archive(filename, extract_dir, compress_type=None):
    """Unpack an archive if it matches tarfile.is_tarfile.

    Args:
      filename: The filename of the given archive file.
      extract_dir: The directory to extract the given archive file.
      compress_type: The type of compression used in the given archive file.

    Returns:
      True if the given file is an archive and False otherwise.
    """
    if tarfile.is_tarfile(filename):
        with tarfile.open(filename) as tar:
            tar.extractall(path=extract_dir)
        return True
    return False


def _unpack_zipfile(filename, extract_dir):
    """Unpack a zip file if it matches zipfile.is_zipfile.

    Args:
      filename: The filename of the given archive file.
      extract_dir: The directory to extract the given archive file.
