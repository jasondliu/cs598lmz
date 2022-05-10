import types
# Test types.FunctionType
try:
    types.FunctionType
except:
    print("SKIP")
    raise SystemExit

# FunctionType args
def f(x):
    return x

print(type(f))
print(type(lambda: None))
print(type(lambda x:x))
print(type(lambda x,y:x+y))
print(type(lambda x=1,y=2:x+y))
print(type(lambda *args: None))
print(type(lambda **kwargs: None))
print(type(lambda *args, **kwargs: None))
