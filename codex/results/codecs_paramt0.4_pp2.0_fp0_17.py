import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import exists, join, dirname

from glob \
    import glob

from distutils.core \
    import setup

from distutils.command.install_data \
    import install_data

from distutils.command.install \
    import install

from distutils.command.build_py \
    import build_py

from distutils.command.build_scripts \
    import build_scripts

from distutils.dep_util \
    import newer

from distutils.errors \
    import DistutilsOptionError

from distutils.sysconfig \
    import get_python_lib

from distutils.core \
    import Command

from distutils.util \
    import get_platform

from distutils.errors \
    import DistutilsSetupError

from distutils.util \
    import convert_path

from distutils.command.build_ext \
    import build_ext

from distutils.
