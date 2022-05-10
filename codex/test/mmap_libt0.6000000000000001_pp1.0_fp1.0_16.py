import mmap
from os import path
import os
import re
import subprocess
import sys

from Cython.Build import cythonize
from setuptools import find_packages, setup
from setuptools.extension import Extension
from setuptools.command.build_ext import build_ext as _build_ext


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def version():
    root = path.abspath(path.dirname(__file__))
    init_path = path.join(root, 'pypcapfile', '__init__.py')
    with open(init_path, 'r') as f:
        init_py = f.read()
        VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
        mo = re.search(VSRE, init_py, re.M)
        if mo:
            return mo.group(1)
