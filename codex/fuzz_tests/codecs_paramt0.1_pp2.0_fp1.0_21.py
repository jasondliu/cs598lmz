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

from sys \
    import exit, argv, stdout, stderr

from time \
    import time

from optparse \
    import OptionParser

from re \
    import compile as re_compile

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, TarInfo

from tempfile \
    import mkdtemp

from distutils.dir_util \
    import copy_tree

from distutils.file_util \
    import
