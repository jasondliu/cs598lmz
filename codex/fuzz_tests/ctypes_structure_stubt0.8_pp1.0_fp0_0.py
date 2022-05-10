import ctypes

class S(ctypes.Structure):
    x = (42, "a")

class S2(ctypes.Structure):
    _fields_ = [("x", (42, "a"))]

for cls in S, S2:
    s = cls()
    s.x = 10
    print(s.x)
    s.x = 20
    print(s.x)
    s.x = "b"
    print(s.x)
    #s.x = ("b", 3)
    #print(s.x)
    s.x = ("b",)
    print(s.x)
    try:
        s.x = (1, 2, 3)
    except TypeError:
        pass
    else:
        print("TypeError not raised")
