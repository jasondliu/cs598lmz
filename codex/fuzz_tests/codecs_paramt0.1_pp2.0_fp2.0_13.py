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

from re \
    import compile, sub

from glob \
    import glob

from optparse \
    import OptionParser

from cPickle \
    import load, dump

from time \
    import time

from cStringIO \
    import StringIO

from cgi \
    import escape

from types \
    import ListType

from codecs \
    import open

from textwrap \
    import wrap

from inspect \
    import getargspec

from cProfile \
    import Profile

from pstats \
    import Stats

from pprint \
    import pprint

from difflib \
    import unified_diff

from traceback \
    import print_exc

from cProfile \
    import Profile

from p
