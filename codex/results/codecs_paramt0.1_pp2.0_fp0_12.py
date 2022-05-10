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
    import argv, exit, stdout

from optparse \
    import OptionParser

from cStringIO \
    import StringIO

from time \
    import time

from re \
    import compile

from glob \
    import glob

from codecs \
    import open

from cPickle \
    import dump, load

from cgi \
    import escape

from markdown \
    import markdown

from docutils.core \
    import publish_parts

from docutils.writers.html4css1 \
    import Writer

from docutils.writers.html4css1 \
    import HTMLTranslator as BaseTranslator

from docutils.writers.html4css1 \
    import HTMLTranslator as BaseTranslator

from docutils.parsers.rst \

