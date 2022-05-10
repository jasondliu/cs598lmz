import types
# Test types.FunctionType()
try:
    f = types.FunctionType(code, globals())
except TypeError as err:
    print(err)

# Test types.CodeType()
try:
    c = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
except TypeError as err:
    print(err)

# Test types.FrameType()
try:
    f = types.FrameType(globals(), {}, '', (), ())
except TypeError as err:
    print(err)
