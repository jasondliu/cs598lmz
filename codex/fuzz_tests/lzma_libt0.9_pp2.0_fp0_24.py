import lzma
lzma.__version__

import struct
struct.__version__

__import__('unittest')
import unittest
unittest.__version__

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import cElementTree as ET
import random
import sys
sys.__version__

import tarfile
tarfile.__version__

import tempfile
tempfile.__version__

import os
import os.path
import zipfile
import contextlib

import coverage
coverage.__version__
