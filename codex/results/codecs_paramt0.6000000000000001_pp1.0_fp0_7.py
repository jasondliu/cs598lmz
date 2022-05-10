import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
# TODO: Should this be 'utf8' or 'utf-8'?
encoding = 'utf8'

# TODO: is this the best way to handle this?
import sys
if sys.version_info >= (3, 0):
    def u(x):
        return x
else:
    def u(x):
        return unicode(x, encoding, 'replace_with_space')

import re
# TODO: is this the best way to handle this?
if sys.version_info >= (3, 0):
    def r(x):
        return re.compile(x)
else:
    def r(x):
        return re.compile(x.encode(encoding))

# TODO: should we be doing this?
import os
os.environ['TZ'] = 'UTC'

import datetime

# TODO: is this the best way to handle this?
if sys.version_info >= (3, 0):
    def type_bytes(x):

