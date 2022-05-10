from types import FunctionType
list(FunctionType(1,2,3,4,5))

from types import ModuleType
list(ModuleType(1,2,3,4,5))

from types import TypeType
list(TypeType(1,2,3,4,5))

try:
    from types import UnboundMethodType
    list(UnboundMethodType(1,2,3,4,5))
except:
    print("SKIP")

# from types import WrapperDescriptorType
# list(WrapperDescriptorType(1,2,3,4,5))

try:
    from types import __build_class__
    list(__build_class__(1,2,3,4,5))
except:
    print("SKIP")

# from types import __import__
# list(__import__(1,2,3,4,5))

# from types import __prepare__
# list(__prepare__(1,2,3,4,5))

# from types import coroutine
# list(coroutine(1,2,3,4,5
