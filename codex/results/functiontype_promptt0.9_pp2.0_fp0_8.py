import types
# Test types.FunctionType
# Functions are first class. function type is correct
def f1(x):
    x[0]++
f1([1,2,3])
print(f1)                                 # <function f1 at 0x7f3a3a2ff268>
