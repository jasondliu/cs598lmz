import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, isdir, isfile, splitext, basename, dirname

from os \
    import listdir, makedirs

from glob \
    import glob

from re \
    import compile

from sys \
    import argv, exit

from time \
    import time

from optparse \
    import OptionParser

from cPickle \
    import load, dump

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, TarInfo, open as taropen

from fnmatch \
    import fnmatch

from shutil \
    import copyfile, copytree, rmtree

from subprocess \
    import Popen, PIPE

from tempfile \
    import mkdtemp

from textwrap \
    import TextWrapper

from logging \
    import
