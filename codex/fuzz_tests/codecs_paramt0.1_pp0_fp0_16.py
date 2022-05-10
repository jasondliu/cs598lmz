import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, exists, abspath

from os \
    import makedirs

from sys \
    import argv, exit

from optparse \
    import OptionParser

from subprocess \
    import Popen, PIPE

from re \
    import compile

from glob \
    import glob

from shutil \
    import copyfile

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
    import DistutilsError

from distutils.spawn \
    import spawn

from distutils.command
