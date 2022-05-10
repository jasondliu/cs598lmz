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

from distutils.command.install_scripts \
    import install_scripts

from distutils.command.sdist \
    import sdist

from distutils.errors \
    import DistutilsOptionError

from distutils.sysconfig \
    import get_python_lib

from distutils.util \
    import get_platform

from distutils.version \
    import LooseVersion

from distutils.command.build_ext \
    import build_ext

from distutils.extension \
    import Extension

from distutils.command.build_clib \
   
