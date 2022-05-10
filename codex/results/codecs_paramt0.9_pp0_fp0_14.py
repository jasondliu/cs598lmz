import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os.path
import re
import sys

from distutils.core import Command
from distutils.command.install import install
from distutils.command.install_data import install_data
from distutils.command.install_egg_info import install_egg_info
from setuptools import setup, find_packages


PACKAGE = "mplipyt"
NAME = "mplipyt"
DESCRIPTION = "A set of scripts for IPython to use matplotlib"
AUTHOR = "Robert T. McGibbon"
AUTHOR_EMAIL = "rmcgibbo@gmail.com"
MAINTAINER = "Robert T. McGibbon"
MAINTAINER_EMAIL = "rmcgibbo@gmail.com"
URL = "http://github.com/rmcgibbo/mplipyt"
LICENSE = "BSD 3-clause"

def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs
