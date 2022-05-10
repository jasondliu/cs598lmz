import mmap
import os
import os.path as osp
import pickle
import re
import shutil
import sys
import tarfile
import tempfile
import zipfile

from six.moves import urllib

from . import config

logger = logging.getLogger(__name__)


def get_download_dir():
    """Return the directory in which downloaded and converted datasets are stored.

    This directory is defined by the environment variable ``CHAINER_DATASET_ROOT``.
    If the environment variable is not specified, it defaults to ``$HOME/.chainer/dataset``.

    Returns:
        str: The path to the download directory.
    """
    return config.get_download_dir()


def get_dataset_directory(dataset_name):
    """Return the directory in which the given dataset is stored.

    Args:
        dataset_name (str): The name of the dataset.

    Returns:
        str: The path to the dataset directory.
    """
    return osp.join(get_download_dir(), dataset_
