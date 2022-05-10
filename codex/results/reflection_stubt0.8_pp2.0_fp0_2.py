fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
codeobject = fn.__code__
codeobject.co_argcount = argcount
codeobject.co_stacksize = stacksize

m = memoryview(b"\x00" * 64)
for i in range(64):
    fn.__code__.co_code[i] = m[i]

try:
    fn(*([1] * argcount))
except SystemError as e:
    print(e)
