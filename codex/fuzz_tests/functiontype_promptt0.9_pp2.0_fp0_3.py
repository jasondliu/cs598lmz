import types
# Test types.FunctionType:
def f(): pass
assert f.__class__ is types.FunctionType
assert type(f) is types.FunctionType
assert (types.FunctionType is
        type(types.FunctionType.__new__(types.FunctionType)))

# Test exceptions:
class E(Exception): pass
class E1(Exception): pass
class E2(E): pass

# Test types.BaseException:
assert type(BaseException) is types.BaseException
assert type(Exception) is types.BaseException
assert type(SystemExit) is types.BaseException
assert type(KeyboardInterrupt) is types.BaseException
assert type(GeneratorExit) is types.BaseException
assert type(StopIteration) is types.BaseException
assert type(StandardError) is types.BaseException
assert type(Warning) is types.BaseException
assert type(BytesWarning) is types.BaseException
assert type(UnicodeWarning) is types.BaseException
assert type(ImportWarning) is types.BaseException
assert type(FutureWarning) is types.BaseException
assert type(UserWarning) is types.BaseException
assert
