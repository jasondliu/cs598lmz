import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, abspath, isdir

from os \
    import makedirs, listdir, walk, remove, rmdir, stat

from stat \
    import ST_MODE

from time \
    import time

from glob \
    import glob

from fnmatch \
    import fnmatch

from re \
    import compile

from sys \
    import argv, exit, stdout, stderr, platform

from optparse \
    import OptionParser

from subprocess \
    import Popen, PIPE

from cStringIO \
    import StringIO

from cPickle \
    import dump, load

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, TarInfo

from tempfile \
    import mkdtemp

from shutil \
    import copyfile, copy
