import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 10
    y = ctypes.c_char * 10
    z = ctypes.c_char * 10

s = S()
s.x = "hello"
s.y = "world"
s.z = "!!!"
print(s.x)
print(s.y)
print(s.z)

s1 = S()
s1.x = "good"
s1.y = "morning"
s1.z = "!!!"
print(s1.x)
print(s1.y)
print(s1.z)

print(s)
print(s1)

s2 = S()
s2.x = "good"
s2.y = "morning"
s2.z = "!!!"
print(s2.x)
print(s2.y)
print(s2.z)

print(s2)

print(s == s1)
print(s1 == s2)
