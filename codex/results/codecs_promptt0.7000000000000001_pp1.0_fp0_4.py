import codecs
# Test codecs.register_error
#
# The tests here are pretty minimal.  Perhaps some more elaborate tests
# are in order, but this is a start.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com) with feedback from
# Martin v. Loewis, Tim Peters and Guido van Rossum.

import sys
import codecs
import encodings
import unittest

# Error handler which returns the original callable
class Handler:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Handler %r>' % self.name

    def __call__(self, exception):
        return exception.object[exception.start:exception.end]

# Error handler which returns a tuple with the original callable and
# the replaced characters (strings)
class TupleHandler:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<TupleHandler %r>' % self.name

    def __call__(self,
