import codecs
# Test codecs.register_error for python 3.x
#
#   codecs.register_error(name, handler)
#
# Registers the specified error handler under the name name. handler
# may be a callable that takes a unicode argument and returns a unicode
# object, or a dictionary mapping unicode ordinals to unicode ordinals,
# strings or None. The latter type of mapping is used to implement
# "replace" and "ignore" handlers.

from test import support
import unittest
from codecs import register_error, CodecInfo
from codecs import lookup as codecs_lookup

# A trivial error handler
def ignore_error(exception):
    return (exception.object[exception.start:exception.end], exception.end)

# A handler that raises an exception
def raise_error(exception):
    raise TypeError

# A handler that replaces the unencodable char with a question mark
def replace_error(exception):
    return ('?', exception.end)

# An encoding error handler that uses a dictionary
def dict_error(exception):
    return {
