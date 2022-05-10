from types import FunctionType
list(FunctionType(lambda: None, globals()))

# The following is not supported by Python 2.7
# from types import LambdaType
# list(LambdaType(lambda: None, globals()))

# The following is not supported by Python 2.7
# from types import MethodType
# list(MethodType(lambda: None, None))

# The following is not supported by Python 2.7
# from types import ModuleType
# list(ModuleType('__builtins__'))

# The following is not supported by Python 2.7
# from types import SimpleNamespace
# list(SimpleNamespace())

# The following is not supported by Python 2.7
# from types import TracebackType
# list(TracebackType())

# The following is not supported by Python 2.7
# from types import _GeneratorWrapper
# list(_GeneratorWrapper(lambda: None))

# The following is not supported by Python 2.7
# from types import _MethodWrapper
# list(_MethodWrapper(lambda: None, None))

# The following is not supported by Python 2.
