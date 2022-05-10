import codecs
# Test codecs.register_error()
import encodings
import itertools
import tempfile
import warnings

from test import mapping_tests, support

# Craig Rodrigues added an iconv implementation for
# FreeBSD using /usr/local/bin/iconv.  Using this,
# you get encodings like
# 'ISO8859-15//TRANSLIT//IGNORE', 'UTF-8//TRANSLIT//IGNORE', etc.

NORMALIZATION_FORM = ('NFC', 'NFKD', 'NFKC', 'NFD', 'NFKD_CF', 'NFKC_CF',
                      'FULLY-NORMALIZED', 'NONE')
# For NFC, we use a decomposed character.
# It's easier to test NFC with a modified string instead of trying
# to modify the unicode database file.
DECOMPOSED_INPUT = 'a\u0308'
COMPOSED_OUTPUT = '\xc3\x83'


@contextlib.contextmanager
def set_locale():
    saved_locale = locale.setlocale(locale.LC
