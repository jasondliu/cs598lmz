import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, abspath, basename, splitext, isdir

from os \
    import listdir, makedirs, remove, walk

from glob \
    import glob

from fnmatch \
    import fnmatch

from re \
    import compile as re_compile

from sys \
    import stdout, stderr

from time \
    import time

from optparse \
    import OptionParser

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, TarInfo

from tempfile \
    import mkdtemp

from shutil \
    import rmtree, copyfileobj

from contextlib \
    import contextmanager

from subprocess \
    import Popen, PIPE

from logging \
    import getLogger

from pkg_resources
