import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, splitext, basename, isdir, isfile

from os \
    import makedirs, listdir, remove, rmdir, walk

from glob \
    import glob

from fnmatch \
    import fnmatch

from re \
    import compile as re_compile

from sys \
    import exc_info

from time \
    import time

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, open as tar_open

from cStringIO \
    import StringIO

from cPickle \
    import dump, load

from hashlib \
    import md5

from logging \
    import getLogger

from pkg_resources \
    import resource_exists, resource_filename, resource_listdir, \
           resource_isdir, resource_stream, resource_string

from traits
