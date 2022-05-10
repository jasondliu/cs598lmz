fn = lambda: None
# Test fn.__code__
fn.__code__ = getattr(fn, '__code__', None) or _empty_code
# Test fn.__globals__
fn.__globals__ = getattr(fn, '__globals__', None) or {}

import os
# Test os.path.isfile
os.path.isfile = getattr(os.path, 'isfile', None) or (lambda path: False)

# Test sys.gettrace
sys.gettrace = getattr(sys, 'gettrace', None) or (lambda: None)

# Test sys.getprofile
sys.getprofile = getattr(sys, 'getprofile', None) or (lambda: None)

# Test sys.settrace
sys.settrace = getattr(sys, 'settrace', None) or (lambda: None)

# Test sys.setprofile
sys.setprofile = getattr(sys, 'setprofile', None) or (lambda: None)

# Test sys.getsizeof
sys.getsizeof = getattr(sys, 'getsizeof', None) or (lambda
