import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, isdir, isfile, abspath

from os \
    import makedirs, listdir, walk, remove, rmdir, stat

from stat \
    import ST_MODE

from glob \
    import glob

from time \
    import time

from fnmatch \
    import fnmatch

from re \
    import compile as re_compile

from sys \
    import stdout

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

from types \
    import StringType, UnicodeType

from codecs \
    import open as codecs_open

from subprocess \
    import Popen, PIPE
