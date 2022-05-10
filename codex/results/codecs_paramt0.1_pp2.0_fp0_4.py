import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists

from os \
    import makedirs

from distutils.core \
    import setup

from distutils.command.install_data \
    import install_data

from distutils.command.install \
    import install

from distutils.command.build \
    import build

from distutils.command.build_py \
    import build_py

from distutils.command.sdist \
    import sdist

from distutils.dep_util \
    import newer

from distutils.log \
    import info, warn, error

from distutils.errors \
    import DistutilsOptionError

from distutils.sysconfig \
    import get_python_lib

from distutils.util \
    import convert_path

from distutils.version \
    import LooseVersion

from glob \
    import glob

from subprocess \
    import Popen, PIPE
