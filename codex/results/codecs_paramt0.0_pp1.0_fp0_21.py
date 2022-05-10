import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, exists

from os \
    import makedirs

from subprocess \
    import Popen, PIPE

from distutils.core \
    import setup

from distutils.command.build_py \
    import build_py

from distutils.command.install_data \
    import install_data

from distutils.command.install_lib \
    import install_lib

from distutils.command.install \
    import install

from distutils.command.sdist \
    import sdist

from distutils.command.build_ext \
    import build_ext

from distutils.errors \
    import DistutilsError

from distutils.sysconfig \
    import get_python_lib

from distutils.version \
    import LooseVersion

from distutils.dep_util \
    import newer

from distutils.spawn \
    import find_executable
