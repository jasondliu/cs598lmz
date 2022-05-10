import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from os.path \
    import join, exists

from os \
    import makedirs

from shutil \
    import copyfile

from distutils.core \
    import setup

from distutils.command.install_data \
    import install_data

from distutils.command.install_lib \
    import install_lib

from distutils.command.build_py \
    import build_py

from distutils.command.sdist \
    import sdist

from distutils.dep_util \
    import newer

from distutils.log \
    import info, warn, error

from distutils import sysconfig

from glob \
    import glob

import sys

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

# The name of the package:
name = 'traits'

# The version of the package:
version = '3.3.0'

# The release status of the package:
release
