import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, exists

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

from distutils.dep_util \
    import newer

from distutils.log \
    import info, warn, error

from distutils.errors \
    import DistutilsOptionError

from distutils.sysconfig \
    import get_python_lib

from distutils.version \
    import LooseVersion

from glob \
    import glob

from subprocess \
    import Popen, PIPE

from sys \
    import version_info

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The name of the package:
name = 'traitsui'


