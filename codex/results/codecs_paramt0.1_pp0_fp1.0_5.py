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

from subprocess \
    import Popen, PIPE

from time \
    import time

from sys \
    import exit, argv, stdout, stderr

from optparse \
    import OptionParser

from re \
    import compile as re_compile

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, open as tar_open

from tempfile \
    import mkdtemp

from contextlib \
    import contextmanager

from distutils.dir_util \
    import copy_
