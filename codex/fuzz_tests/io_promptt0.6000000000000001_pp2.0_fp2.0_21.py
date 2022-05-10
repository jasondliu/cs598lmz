import io
# Test io.RawIOBase
import sys
import time

from test import support
from test.support import _2G, _4G

# Isolated filesytem to test file.truncate() on.
ISOLATED_FN = support.TESTFN + "isolated"
ISOLATED_SYMLINK = support.TESTFN + "isolated_symlink"
ISOLATED_DIR = support.TESTFN + "isolated_dir"

def create_file(name, contents):
    with open(name, "wb") as f:
        f.write(contents)

def create_isolated_file():
    try:
        os.mkdir(ISOLATED_DIR)
    except FileExistsError:
        pass
    create_file(ISOLATED_FN, b"aaa")
    os.symlink(ISOLATED_FN, ISOLATED_SYMLINK)

def cleanup_isolated_file():
    try:
        os.unlink(ISOLATED_FN)
        os.unlink(ISOLATED_SYMLINK)
       
