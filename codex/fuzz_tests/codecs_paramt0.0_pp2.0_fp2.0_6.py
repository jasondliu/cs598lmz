import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, isdir, isfile

from os \
    import makedirs, listdir, walk, remove, rmdir, stat

from stat \
    import ST_MODE, S_IWRITE

from time \
    import time

from glob \
    import glob

from fnmatch \
    import fnmatch

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, TarInfo

from cStringIO \
    import StringIO

from cPickle \
    import dump, load

from hashlib \
    import md5

from re \
    import compile as re_compile

from sys \
    import exc_info

from traceback \
    import format_exception

from logging \
    import getLogger

from optparse \
    import OptionParser

from types
