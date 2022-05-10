import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, abspath, basename, splitext

from os \
    import makedirs

from sys \
    import argv, exit

from glob \
    import glob

from re \
    import compile, sub

from optparse \
    import OptionParser

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, TarInfo

from shutil \
    import copyfileobj, rmtree

from subprocess \
    import Popen, PIPE

from time \
    import time

from codecs \
    import open

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The name of the file containing the list of files to include in the package:
PackageFile = 'package.txt'

# The name of the file containing the list of files to
