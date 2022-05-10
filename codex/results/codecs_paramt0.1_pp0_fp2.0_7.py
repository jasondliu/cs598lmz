import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, isdir, abspath

from os \
    import makedirs, listdir, remove, walk

from glob \
    import glob

from fnmatch \
    import fnmatch

from re \
    import compile, sub

from sys \
    import exit, stdout, stderr

from time \
    import time, localtime, strftime

from optparse \
    import OptionParser

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
    import rmtree, copyfileobj

from subprocess \
    import Popen, PIPE

from logging \
    import getLogger
