import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

a = S()
a.x = 3
a.y = 4

b = S()
b.x = 7
b.y = 8

S.x.__doc__ = "3"
S.y.__doc__ = "4"

for field in S._fields_:
    print("{}: {}".format(field[0], field[1].__doc__))

print("x: {}".format(a.x))
print("y: {}".format(a.y))
print("x: {}".format(b.x))
print("y: {}".format(b.y))
</code>
Output:
<code>x: 3
y: 4
x: 3
y: 4
x: 7
y: 8
</code>
I want to store the documentation, so I can retrieve it without constantly reading from the Python code.


A:

The documentation is stored in the _type_ structure. From the documentation:
<blockquote>
<p><code>&lt
