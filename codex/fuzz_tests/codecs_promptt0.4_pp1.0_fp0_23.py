import codecs
# Test codecs.register_error
#
# The codecs module is not part of the standard library in Python 2.2,
# so we have to check for its presence.

try:
    import codecs
except ImportError:
    raise ImportError("this test needs the 'codecs' module")

import unittest
import test.test_support

# Error handler that replaces the unencodable character with a question mark.
def replace_with_question_marks(error):
    return (u'?', error.start + 1)

# Error handler that replaces the unencodable character with an X.
def replace_with_x(error):
    return (u'X', error.start + 1)

# Error handler that inserts an extra character before the unencodable
# character.
def insert_extra_character(error):
    return (u'ab', error.start + 1)

# Error handler that inserts an extra character before the unencodable
# character and replaces the unencodable character with an X.
def insert_extra_character_and_replace_with_x(error):
   
