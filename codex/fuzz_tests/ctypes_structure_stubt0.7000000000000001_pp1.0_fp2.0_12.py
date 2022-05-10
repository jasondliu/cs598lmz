import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float * 4
    z = ctypes.c_float * 4 * 4

def main():
    s = S()
    print s.x
    print s.y
    print s.z

if __name__ == "__main__":
    main()
</code>
S.z is a list of lists. I want to print the entire object with all the elements. Is there a quick way to do this using some recursion?


A:

The simplest way is to use the <code>pprint</code> module.
<code>from pprint import pprint

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_float * 4),
                ("z", ctypes.c_float * 4 * 4)]

s = S()
pprint(s.__dict__)
</code>
Output
<code>{'x': 0,
 'y': (_ctypes.c_float(0.0),
