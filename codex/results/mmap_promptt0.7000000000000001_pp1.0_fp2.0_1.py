import mmap
# Test mmap.mmap()
import os

# Test os.getcwd()
import pwd
# Test pwd.getpwuid()
import random
# Test random.randint()
import re
# Test re.match()
import shutil
# Test shutil.copy()
import subprocess
# Test subprocess.Popen()
import sys
# Test sys.exit()
import tarfile
# Test tarfile.TarFile()
import time
# Test time.sleep()
import traceback
# Test traceback.format_exc()
import unittest
# Test unittest.TestCase()
import urllib
# Test urllib.urlretrieve()
import urllib2
# Test urllib2.urlopen()
import uuid
# Test uuid.uuid4()
import zipfile
# Test zipfile.ZipFile()

from filecmp import cmp
from os.path import exists, isfile
from subprocess import Popen, PIPE

class ModuleImportTest(unittest.TestCase):
    def test_import(self):
        "Test import of
