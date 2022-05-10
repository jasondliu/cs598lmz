import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

a = S()
a.x = 1
a.y = 2
a.z = 3

b = S()
b.x = 4
b.y = 5
b.z = 6

c = S()
c.x = 7
c.y = 8
c.z = 9

d = S()
d.x = 10
d.y = 11
d.z = 12

e = S()
e.x = 13
e.y = 14
e.z = 15

f = S()
f.x = 16
f.y = 17
f.z = 18

g = S()
g.x = 19
g.y = 20
g.z = 21

h = S()
h.x = 22
h.y = 23
h.z = 24

i = S()
i.x = 25
i.y = 26
i.z = 27

j = S()
j.x = 28

