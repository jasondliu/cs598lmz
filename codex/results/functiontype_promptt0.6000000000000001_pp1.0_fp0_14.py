import types
# Test types.FunctionType
try:
    f = types.FunctionType(types.CodeType(0, 0, 0, 0, 0, b"", (), (), (), "", "", 0, b""), {})
except TypeError:
    print("SKIP")
    raise SystemExit

def func():
    pass

print(type(func))
print(type(func.__code__))
print(type(func.__code__.co_code))

# Test types.FrameType
import sys
import _testcapi

def f():
    try:
        raise _testcapi.make_exc('frame')
    except _testcapi.make_exc('frame') as e:
        _testcapi.raise_exc(e.__cause__)

try:
    f()
except _testcapi.make_exc('frame') as e:
    print(type(e.__traceback__))
    print(type(e.__traceback__.tb_frame))
    print(type(e.__traceback__.tb_frame.f_code))

