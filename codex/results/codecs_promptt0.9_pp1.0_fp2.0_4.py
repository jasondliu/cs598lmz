import codecs
# Test codecs.register_error
import abc
# Test abc.ABCMeta
import operator
# Test operator.itemgetter
import itertools
# Test itertools.chain
import _string
# Test _unicode sort
import collector
# Test that collector loads cleanly
import __builtin__
# Test use of __builtin__.True, etc.
import StringIO
# Test that StringIO loads cleanly
import _io
# Test that _io loads cleanly
import inspector
# Test that inspector loads cleanly
import _warnings
# Test that _warnings loads cleanly
import curses.ascii
# Test curses.ascii.islower
import warnings
# Test warnings.warn, but avoid doing anything if warnings are being ignored
# by default.
[help(warnings.warn)]
import keyword
# Test keyword.kwlist
import functools
# Test functools.partial
import locale
# Test locale.getpreferredencoding
import socket, types, select
# Test specific things having to do with the C API. These modules have to be
# imported to generate the C API.
del socket,
