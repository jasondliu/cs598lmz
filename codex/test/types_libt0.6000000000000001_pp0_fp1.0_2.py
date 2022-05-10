import types
types.ClassType

# Test 2
#
# Test whether the module-level builtin functions are
# in the __builtin__ module.

import __builtin__

__builtin__.__dict__.has_key('abs')
__builtin__.__dict__.has_key('apply')
__builtin__.__dict__.has_key('buffer')
__builtin__.__dict__.has_key('callable')
__builtin__.__dict__.has_key('chr')
__builtin__.__dict__.has_key('cmp')
__builtin__.__dict__.has_key('coerce')
