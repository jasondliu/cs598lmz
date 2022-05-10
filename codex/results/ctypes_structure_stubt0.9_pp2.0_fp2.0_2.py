import ctypes

class S(ctypes.Structure):
    x = 2

for i in range(4)[::-1]:
    print(S((i, ))[0])


if len(S()) > 0:
    print(S()[0])
