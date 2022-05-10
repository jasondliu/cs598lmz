import mmap
import os
import re
import shutil
import sys
import tempfile
import time
import unittest

from test import support
from test.support import import_helper

import_helper.import_module('tarfile')
tarfile = sys.modules['tarfile']

import_helper.import_module('zipfile')
zipfile = sys.modules['zipfile']

def make_tarname(name):
    return os.path.join("tmp", name)

def make_test_tarfile(name, mode="w:", members=()):
    tar = tarfile.open(name, mode)
    for member in members:
        tar.addfile(member)
    tar.close()

def make_test_zipfile(name, mode="w", members=()):
    zip = zipfile.ZipFile(name, mode)
    for member in members:
        zip.writestr(member, "")
    zip.close()

