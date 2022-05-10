import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, isdir, isfile

from os \
    import makedirs, listdir, walk, remove, rmdir

from glob \
    import glob

from shutil \
    import copyfile, copytree, rmtree

from zipfile \
    import ZipFile, ZIP_DEFLATED

from subprocess \
    import Popen, PIPE

from sys \
    import argv, exit, stdout, stderr

from optparse \
    import OptionParser

from time \
    import time

from re \
    import compile as re_compile

from cStringIO \
    import StringIO

from cPickle \
    import dump, load

from hashlib \
    import md5

from logging \
    import getLogger

from logging.handlers \
    import RotatingFileHandler

from threading
