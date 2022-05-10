import ctypes

class S(ctypes.Structure):
    x = ctypes.c_wchar_p
    y = ctypes.c_wchar_p

s = S()

s.x = "test".encode("utf-8")
s.y = "test".encode("utf-8")

print(s.x)
print(s.y)
