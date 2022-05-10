import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join

from distutils.core \
    import setup

from distutils.command.install_data \
    import install_data

from distutils.command.install_lib \
    import install_lib

from distutils.command.build_py \
    import build_py

from distutils.command.build_scripts \
    import build_scripts

from distutils.command.sdist \
    import sdist

from distutils.dep_util \
    import newer

from distutils.log \
    import info, warn

from distutils.errors \
    import DistutilsOptionError

from distutils.sysconfig \
    import get_python_lib

from distutils import dir_util

from glob \
    import glob

from os \
    import getcwd, listdir, makedirs, remove, walk, environ

from os.path \
    import abspath, basename,
