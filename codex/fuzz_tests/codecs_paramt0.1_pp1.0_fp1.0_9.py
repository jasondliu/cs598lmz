import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, isdir, isfile, abspath

from os \
    import makedirs, listdir, walk, remove, rmdir, stat

from stat \
    import ST_MODE

from codecs \
    import open

from re \
    import compile as re_compile

from time \
    import time

from sys \
    import exit, argv, stdout, stderr

from optparse \
    import OptionParser

from cPickle \
    import dump, load

from hashlib \
    import md5

from glob \
    import glob

from fnmatch \
    import fnmatch

from cStringIO \
    import StringIO

from subprocess \
    import Popen, PIPE

from cgi \
    import escape

from tempfile \
    import mkdtemp

from shutil \

