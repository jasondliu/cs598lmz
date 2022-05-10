import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, abspath, exists, isdir, isfile, splitext, basename

from os \
    import makedirs, listdir, remove, walk, rmdir, stat

from stat \
    import ST_MTIME

from time \
    import time

from glob \
    import glob

from re \
    import compile, search, sub

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

from hashlib \
    import md5

from codecs \
    import open as codecs_open

from logging \
    import getLogger

from logging.handlers \
    import RotatingFileHandler

from threading \

