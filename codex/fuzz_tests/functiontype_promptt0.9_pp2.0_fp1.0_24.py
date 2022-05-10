import types
# Test types.FunctionType
#!assert isinstance(len, types.FunctionType)
#!assert isinstance(test.test_descr, types.FunctionType)
# Test types.MethodType
#!assert isinstance(test.test_descr.__call__, types.MethodType)

import operator
import copy_reg
# Test types.MethodType
#!assert isinstance(operator.isCallable, types.MethodType)
# Test copy_reg.constructor
#!assert isinstance(copy_reg._reconstructor, copy_reg.constructor)

# Test module type
#!assert isinstance(operator, types.ModuleType)

# Test 'unknown' type
#!assert isinstance(exec, types.Unknown)

# Test unittest
#!assert isinstance(1, int)

#!assert isinstance(1, long)

#!assert isinstance(1, float)

#!assert not isinstance(1, types.BooleanType)

class InstClass:
    pass

#!assert isinstance(InstClass(), InstClass)

#!
