import lzma
lzma.LZMAFile()

#(3,5,5)

from types import ModuleType
import types

import moduletest

# StringIO and cStringIO are not there unconditionally.
try:
    import StringIO
except ImportError:
    pass
else:
    StringIO()

try:
    import cStringIO
except ImportError:
    pass
else:
    cStringIO.StringIO()

#(3,6,0)

import io
import _pyio
import weakref

# We import encodings.idna in order to trigger the auto-generated aliases.
# http://bugs.python.org/issue28850
import encodings.idna

# Ensure we can load the C implementation of pickle.
import _pickle

# Unicode aliases
import unicodedata
unicodedata.unidata_version == '8.0.0'

#(3,6,1)

# IMAP4 is not there unconditionally
try:
    import imaplib
except ImportError:
    pass
else
