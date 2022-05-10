gi = (i for i in ())
# Test gi.gi_code is None.

class C(A):
    def __init__(self):
        self.i = 0
        self.gi = (i for i in range(5))

c = C()
print(c.gi.gi_frame.f_locals)
print(c.gi.gi_frame.f_locals['i'])
print(">>> next(c.gi)")
print("3")
print(">>> next(c.gi)")
print("2")
print(">>> next(c.gi)")
print("1")
print(">>> next(c.gi)")
print("0")
print(">>> list(c.gi)")
print("[]")
print(">>> c.gi.gi_frame.f_locals['i']")
print("-2")
print(">>> list(c.gi)")
print("[]")
