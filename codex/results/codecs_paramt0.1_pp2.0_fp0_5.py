import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, abspath, exists

from os \
    import makedirs

from sys \
    import argv, exit

from glob \
    import glob

from re \
    import compile, sub

from optparse \
    import OptionParser

from cStringIO \
    import StringIO

from zipfile \
    import ZipFile, ZIP_DEFLATED

from tarfile \
    import TarFile, TarInfo

from shutil \
    import copyfileobj, rmtree

from subprocess \
    import Popen, PIPE

from time \
    import time

from textwrap \
    import dedent

from cPickle \
    import load, dump

from cgi \
    import escape

from urllib \
    import quote

from xml.sax.saxutils \
    import escape as xml_escape

from xml.dom.minid
