import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, exists

from os \
    import makedirs

from sys \
    import argv

from glob \
    import glob

from re \
    import compile

from shutil \
    import copyfile

from optparse \
    import OptionParser

from subprocess \
    import Popen, PIPE

from time \
    import time

from cStringIO \
    import StringIO

from cPickle \
    import load, dump

from zipfile \
    import ZipFile

from tarfile \
    import TarFile

from tempfile \
    import mkdtemp

from distutils.dir_util \
    import copy_tree

from distutils.file_util \
    import copy_file

from distutils.errors \
    import DistutilsFileError

from distutils.command.build_py \
    import build_py

from distutils
