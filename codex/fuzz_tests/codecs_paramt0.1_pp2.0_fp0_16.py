import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, isdir, isfile

from os \
    import makedirs, listdir, remove, walk

from shutil \
    import copyfile, copytree, rmtree

from glob \
    import glob

from re \
    import compile, sub

from sys \
    import argv, exit, stdout

from time \
    import time

from optparse \
    import OptionParser

from subprocess \
    import Popen, PIPE

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, TarInfo

from tempfile \
    import mkdtemp

from cPickle \
    import load, dump

from hashlib \
    import md5

from logging \
    import getLogger

from logging.
