import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, splitext, basename, isdir, isfile

from os \
    import makedirs, listdir, remove, walk, rmdir

from shutil \
    import copyfile, copytree, rmtree

from glob \
    import glob

from zipfile \
    import ZipFile, ZIP_DEFLATED

from subprocess \
    import Popen, PIPE

from time \
    import time

from re \
    import compile as re_compile

from sys \
    import argv, exit, stdout, stderr

from optparse \
    import OptionParser

from cStringIO \
    import StringIO

from cPickle \
    import load, dump

from hashlib \
    import md5

from logging \
    import getLogger

from logging.handlers \
    import RotatingFileHandler

from threading
