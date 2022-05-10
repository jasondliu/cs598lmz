import mmap
import os
import re
import shutil
import stat
import sys
import tempfile

from distutils.command.build import build
from distutils.command.clean import clean
from distutils.command.install_data import install_data
from distutils.command.install_scripts import install_scripts
from distutils.core import setup
from distutils.sysconfig import get_python_lib

#-------------------------------------------------------------------------------
#
# Constants
#
#-------------------------------------------------------------------------------

#
# Name of the package
#
PACKAGE_NAME = 'pymatgen'

#
# Package version
#
PACKAGE_VERSION = open('VERSION').read().strip()

#
# Package description
#
PACKAGE_DESCRIPTION = 'Python Materials Genomics is a robust materials analysis code that defines core object representations for structures and molecules with support for many electronic structure codes. It is currently the core analysis code powering the Materials Project (https://www.materialsproject.org).'

#
