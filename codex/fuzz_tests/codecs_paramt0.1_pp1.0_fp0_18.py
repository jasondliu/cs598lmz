import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, isdir, isfile, abspath

from os \
    import listdir, makedirs, remove, walk

from glob \
    import glob

from shutil \
    import copyfile

from re \
    import compile, search, sub

from sys \
    import argv, exit, stdout, stderr, version_info

from optparse \
    import OptionParser

from time \
    import time

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, TarInfo

from tempfile \
    import mkdtemp

from subprocess \
    import Popen, PIPE

from cPickle \
    import dump, load

from hashlib \
    import md5

from codecs \
    import open
