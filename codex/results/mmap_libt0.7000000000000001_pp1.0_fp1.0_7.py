import mmap
import os
import re
import subprocess
import sys
import tempfile

from itertools import chain
from os.path import join

from distutils import errors
from distutils import log
from distutils import sysconfig

from distutils.core import Command
from distutils.core import Extension
from distutils.core import setup

from distutils.command.build_ext import build_ext
from distutils.command.build_scripts import build_scripts
from distutils.command.clean import clean
from distutils.command.egg_info import egg_info
from distutils.command.install import install
from distutils.command.install_data import install_data
from distutils.command.install_scripts import install_scripts
from distutils.command.sdist import sdist
from distutils.command.upload import upload

from distutils.spawn import find_executable

try:
  from Cython.Distutils import build_ext
  cmdclass = {'build_ext': build_ext}
except ImportError:
  cmdclass = {}

try:
  import pkg_resources
