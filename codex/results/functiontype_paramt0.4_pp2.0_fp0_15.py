from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# from types import LambdaType
# list(LambdaType(lambda: None, globals(), 'lambda'))

# from types import MethodType
# list(MethodType(lambda: None, None, None))

# from types import CodeType
# list(CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b''))

# from types import MappingProxyType
# list(MappingProxyType({}))

# from types import SimpleNamespace
# list(SimpleNamespace())

# from types import DynamicClassAttribute
# list(DynamicClassAttribute())

# from types import get_type_hints
# list(get_type_hints(list))

# from types import coroutine
# list(coroutine(lambda: None))

# from types import AsyncGeneratorType
# list(AsyncGeneratorType(lambda: None, {}))

# from types import AsyncIterable
# list(AsyncIterable())

# from types import AsyncIterator
