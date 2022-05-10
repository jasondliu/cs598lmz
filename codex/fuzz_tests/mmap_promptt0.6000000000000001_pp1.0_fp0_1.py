import mmap
# Test mmap.mmap(0, mmap.PAGESIZE)

import os

print(os.environ)

# Test os.environ.items()

import parser
# Test parser.expr("a + b")

import plistlib
# Test plistlib.dumps({})

import pydoc
# Test pydoc.help("sys")

import py_compile
# Test py_compile.compile("test.py")

import pyclbr
# Test pyclbr.readmodule("sys")

import py_compile
# Test py_compile.compile("test.py")

import pyclbr
# Test pyclbr.readmodule("sys")

import re
# Test re.compile("(?P<name>.*)")

import readline
# Test readline.parse_and_bind("tab: complete")

import selectors
# Test selectors.DefaultSelector()

import shlex
# Test shlex.split("-a -b")

import shutil
# Test shutil.rmtree("tmp")
