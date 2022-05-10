fn = lambda: None
# Test fn.__code__.co_filename

import sys
from test import support

code = fn.__code__

if code is None:
    print("None")
else:
    print(code.co_filename)

if hasattr(sys, 'getfilesystemencoding'):
    print(code.co_filename.encode(sys.getfilesystemencoding()))

support.reap_children()
