import ctypes
ctypes.cast(id(x), ctypes.py_object).value

x = [1, 2, 3]
y = x
z = [1, 2, 4]
c = [x,y,z]
a = [1,2,c]

d = {'a': 1, 2:'b', 'c' : x}
e = {'a': 1, 2:'b', 'c' : y}
f = {'a': 1, 2:'b', 'c' : z}

g = {'a': 1, 'b' : d, c : e}

h = [d, 'a', g]

def rec(val):
    if type(val) == type([]):
        print("List")
        print(repr(val))
        for item in val:
            rec(item)
    elif type(val) == type({}):
        print("Dict")
        print(re
