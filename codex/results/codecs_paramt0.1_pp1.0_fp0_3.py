import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, exists, splitext, basename, isdir, isfile

from os \
    import makedirs, listdir, remove

from glob \
    import glob

from shutil \
    import copyfile

from subprocess \
    import Popen, PIPE

from sys \
    import exit, argv

from time \
    import time

from optparse \
    import OptionParser

from re \
    import compile as re_compile

from codecs \
    import open as codecs_open

from cPickle \
    import load as pickle_load, dump as pickle_dump

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tempfile \
    import mkdtemp

from distutils.dir_util \
    import copy_tree

from distutils.file_util
