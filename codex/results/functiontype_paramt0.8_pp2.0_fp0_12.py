from types import FunctionType
list(FunctionType(x.__code__,x.__globals__,x.__name__,x.__defaults__,x.__closure__) \
        for x in map(lambda x:x.__reduce__()[0],map(lambda x:type(x)==FunctionType, filter(lambda x:x.__module__=='pickle' and type(x)==FunctionType, pickle.__dict__.values()))))

# Output:
[<function opcodes at 0x10cbe17b0>, <function whichmodule at 0x10cbe18e0>, <function _Pickler_dispatch at 0x10cbe1a60>, <function _Pickler at 0x10cbe1b00>, <function _Pickler_impl at 0x10cbe1c18>, <function _Pickler_write at 0x10cbe1c88>, <function dump at 0x10cbe1cf8>, <function dumps at 0x10cbe1d68>, <function _Unpickler_dispatch at 0x10cbe1df0>, <function _Unpickler at
