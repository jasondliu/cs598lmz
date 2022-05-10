import mmap
import os
import pyproj
import re
import shapely.geometry
import time
import xml.etree.ElementTree as ET

from pyproj import transform
from pyproj import Proj


def file_size(fname):
    """
    Returns the size of a file in bytes.
    """
    return os.path.getsize(fname)


def file_size_mib(fname):
    """
    Returns the size of a file in MiB.
    """
    return file_size(fname)/1048576.0


def file_size_gib(fname):
    """
    Returns the size of a file in GiB.
    """
    return file_size(fname)/1073741824.0


def file_to_string(path):
    with open(path, 'r') as f:
        return f.read()


def string_to_file(s, path):
    with open(path, 'w') as f:
        f.write(s)


def replace_in_file(
