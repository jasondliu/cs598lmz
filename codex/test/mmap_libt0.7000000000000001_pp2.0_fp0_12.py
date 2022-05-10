import mmap
import os
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import zipfile
from distutils.version import StrictVersion

from zorg.driver import Driver
from zorg.error import *

if sys.platform == 'win32':
    from zorg.win32_build import *
else:
    from zorg.unix_build import *

class LLVMBuildDriver(Driver):

    def __init__(self, options):
        Driver.__init__(self, options)
        self.llvm_src_dir = os.path.join(self.build_dir, "llvm")
        self.clang_src_dir = os.path.join(self.build_dir, "clang")
        self.clang_tools_extra_src_dir = os.path.join(self.build_dir, "clang-tools-extra")
