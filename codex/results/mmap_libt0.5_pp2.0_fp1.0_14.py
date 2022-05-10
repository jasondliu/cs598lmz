import mmap
import os
import shutil
import subprocess
import tempfile
import time
import unittest

from avocado.utils import process
from avocado.utils import script


basedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
basedir = os.path.abspath(basedir)

AVOCADO = os.environ.get("UNITTEST_AVOCADO_CMD", "./scripts/avocado")

AVOCADO_TEST_SKIP = os.environ.get("AVOCADO_TEST_SKIP", "")


class Avocado(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix='avocado_' + __name__)

    def test_config_datadir(self):
        os.chdir(basedir)
        cmd_line = ('%s config --datadir %s' % (AVOCADO, self.tmpdir))
       
