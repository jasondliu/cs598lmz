import mmap
# Test mmap.mmap
# from mmap import mmap
from os.path import getsize as getFileSize

from . import lib
from .lib import (
    SRC, SRC_SIZE,
    SRC_A, SRC_A_SIZE,
    SRC_B, SRC_B_SIZE,
    SRC_C, SRC_C_SIZE,
    SRC_D, SRC_D_SIZE,
    SRC_E, SRC_E_SIZE,
    SRC_F, SRC_F_SIZE,
    SRC_G, SRC_G_SIZE
)
# Test full name
# import iorequests.lib as lib

# Test as from iorequests import lib
# from iorequests import lib


class TestConditionalIdExist(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
