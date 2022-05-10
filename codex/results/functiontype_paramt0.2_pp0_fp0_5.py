from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Issue #15: http://code.google.com/p/python-virtualenv/issues/detail?id=15
# The following should not raise an exception.
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'test_support'))
import test_support

# Issue #16: http://code.google.com/p/python-virtualenv/issues/detail?id=16
# The following should not raise an exception.
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'test_support'))
import test_support

# Issue #17: http://code.google.com/p/python-virtualenv/issues/detail?id=17
# The following should not raise an exception.
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'test_support'))
import test
