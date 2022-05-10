import mmap
import os
import shutil
import sys
import subprocess
import tempfile
import re
import py
import glob
from rpython.tool.udir import udir
from rpython.rlib.rarithmetic import intmask
from rpython.rlib import rfile, rpath, rposix, rlinkloop
from rpython.rtyper.lltypesystem import lltype, rffi
from rpython.rtyper.lltypesystem.lloperation import llop
from rpython.rtyper.tool import rffi_platform
from rpython.translator.c import gc
from rpython.translator.c.distutils import Extension
from rpython.translator.tool.cbuild import ExternalCompilationInfo
from rpython.translator.platform import platform
from rpython.translator.interactive import Translation


def setup_module_cleanup(module):
    def remove_tmpdir():
        shutil.rmtree(str(module._tmpdir))
    module._tmpdir.ensure(dir=1)
    module._tmpdir.chmod(0777)
