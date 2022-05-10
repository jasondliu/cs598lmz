import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __init__(self):
        self.x.value = 42

l = [S() for i in range(5)]

l[0].x.value = 1
for i in range(1, 5):
    l[i].x.value = l[i-1].x.value

print l[-1].x.value


# this is the original example from the manual
x = ctypes.c_int(1)
l = [x, x]
l[0].value = 2
print l[1].value
# outputs 2


# This is the new example:
l = [ctypes.c_int(i) for i in range(5)]
print l[0].value
print l[1].value
print l[2].value
print l[3].value
print l[4].value

l = [ctypes.c_int(i) for i in range(5)]
l[0].value = 1
for i in range(1, 5):
    l[i].value = l[i-
