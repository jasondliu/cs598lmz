import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, isdir, isfile

from os \
    import makedirs, listdir, walk, remove, rmdir, rename

from glob \
    import glob

from shutil \
    import copyfile, copytree, rmtree

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, open as taropen

from tempfile \
    import mkdtemp

from subprocess \
    import Popen, PIPE

from cStringIO \
    import StringIO

from cPickle \
    import load, dump

from time \
    import time

from re \
    import compile as re_compile

from sys \
    import stdout, stderr, exit, argv, platform

from optparse \
    import OptionParser

from logging \
    import getLog
