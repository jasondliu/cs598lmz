import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, isdir, isfile, splitext, basename, dirname, abspath

from os \
    import listdir, makedirs, remove

from glob \
    import glob

from re \
    import compile

from sys \
    import exit, stdout, stderr, argv

from time \
    import time

from optparse \
    import OptionParser

from cPickle \
    import dump, load

from cStringIO \
    import StringIO

from tarfile \
    import TarFile, TarInfo

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tempfile \
    import mkdtemp

from shutil \
    import rmtree, copyfileobj

from subprocess \
    import Popen, PIPE

from cgi \
    import escape

from types \
    import StringTypes

from pprint \
