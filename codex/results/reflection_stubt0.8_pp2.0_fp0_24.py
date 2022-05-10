fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gi.__code__
gir = gi.__reduce__()
print(gir[0] is type(gi))
print(gir[1] == (fn,))
print(gir[2] == None)

# test __reduce_ex__
import pickle
import sys

# Bug #1270534
class C:
    def __reduce_ex__(self, protocol):
        print("__reduce_ex__ called with protocol", protocol)
        return 1, 2, 3

for proto in range(pickle.HIGHEST_PROTOCOL + 1):
    print("protocol", proto)
    C().__reduce_ex__(proto)

# Bug #1270534
class C:
    def __reduce__(self):
        print("__reduce__ called")
        return 1, 2, 3

C().__reduce__()

# Bug #1270534
class C:
    def __reduce__(self):
        global __sizeof__
        print("
