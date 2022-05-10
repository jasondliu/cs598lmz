import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, splitext, basename, abspath

from os \
    import makedirs

from sys \
    import argv, exit, stdout

from glob \
    import glob

from re \
    import compile, sub

from optparse \
    import OptionParser

from cPickle \
    import load, dump

from time \
    import time

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile

from tarfile \
    import TarFile

from tempfile \
    import mkdtemp

from shutil \
    import rmtree

from subprocess \
    import Popen, PIPE

from cgi \
    import escape

from urllib \
    import quote

from urllib2 \
    import urlopen, HTTPError

from xml.sax.saxutils \
    import
