import io
# Test io.RawIOBase
with io.BytesIO() as f:
    f.write('abc')
    data = f.getvalue()
    assert data == b'abc'
# Test C extensions
import array
import bz2
import gzip
import json
import md5
import nis
import ssl
import sys
import termios
buf = array.array('i', [0] * 10)
buf[5] = -1


def func(a1, a2, a3):
    print('sigma', a1, a2, a3)
    print(a1, a2, a3)
    print('sum:', sum(buf))


func(1, 2, 3)

# Test builtins / stdlib
import abc
import code
import cmd
import collections
import commands
import compiler
import contextlib
import datetime
import distutils.errors
import doctest
import gc
import keyword
import opcode
import pickle
import pkgutil
import pstats
import py_compile
import select
import shutil
import struct
import symbol
import tempfile
