fn = lambda: None
# Test fn.__code__.co_varnames:
setattr(fn, '__code__', CodeType(0, 0, 0, 0, 0, "<string>", "<string>", 0, "<string>", (), (), (), "", "", 0, ""))
setattr(fn, '__defaults__', ())
setattr(fn, '__doc__', '')
setattr(fn, '__globals__', {'__builtins__':dict(__name__='builtins', __doc__='Built-in functions, exceptions, and other objects.', __package__='', __loader__=<class '_frozen_importlib.BuiltinImporter'>, __spec__=None, __annotations__={}, __build_class__=<built-in function __build_class__>, __import__=<built-in function __import__>, __import_meta__=<built-in function __import_meta__>, __spec_staticmethod=<function Spec.__new__.StaticMethodSpec at 0x2c0da78>, __spec_classmethod=<function Spec.__new__.ClassMethodSpec at
