import types
# Test types.FunctionType
function = lambda a: a
assert isinstance(function, types.FunctionType)
# Test types.LambdaType
function = types.LambdaType(
    arg_defs=(
        (('a',), None, None, None),
    ),
    name='<lambda>',
    qualname='<lambda>',
    code=types.CodeType(
        argcount=1,
        posonlyargcount=0,
        kwonlyargcount=0,
        nlocals=1,
        stacksize=2,
        flags=1,
        codestring=(
            b'\x91\x7f' # LOAD_FAST 0 (a)
            b'\x01' # RETURN_VALUE
        ),
        constants=(),
        names=(),
        varnames=('a',),
        filename='<lambda>',
        name='<lambda>',
        firstlineno=1,
        lnotab=(
            b'\x01\x00' # 1 line, 0 offset
        ),
        freevars=(),

