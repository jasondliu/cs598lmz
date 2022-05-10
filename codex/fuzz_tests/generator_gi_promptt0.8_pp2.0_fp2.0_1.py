gi = (i for i in ())
# Test gi.gi_code.co_freevars
assert type(gi.gi_code).__name__ == 'code'
assert gi.gi_code.co_freevars == ('i',)

import sys
assert sys.version_info.major == 3
assert sys.version_info.minor == 4
assert sys.version_info.micro == 0

import os
assert os.path.sep == '/'
assert os.path.altsep is None
assert os.path.extsep == '.'
assert os.path.pathsep == ':'
assert os.path.devnull == '/dev/null'

import re
assert re.compile("a", re.IGNORECASE).flags == re.IGNORECASE

# Test heap-allocated objects/types
import _functools
assert _functools.partial is functools.partial
assert type(_functools.partial) is types.BuiltinFunctionType

import _collections
assert _collections.deque is collections.deque
assert type(_collections.deque) is types.ClassType

