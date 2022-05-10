import mmap
import re
import os
import shutil
import sys
import glob
import pypandoc

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from distutils.command.build_ext import build_ext
from distutils.command.build import build

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as build_ext_original
from pkg_resources import parse_version

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Convert README to reStructuredText
readme_path = path.join(this_directory, 'README.rst')
with open(readme_path, 'w') as f:
    f.write(pypandoc.convert_file('README.md', 'rst'))

#
