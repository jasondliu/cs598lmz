import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

"""

# load the module
mod = imp.new_module('mod')
mod.__file__ = 'mod.py'
exec(code in mod.__dict__)

# run the module
mod.main()

# verify that it was collected
gc.collect()
gc.collect()
if len(gc.garbage) != 1:
    print(len(gc.garbage))
    raise TestFailed("module not collected")

# verify that the reference to the class is gone
try:
    c = mod.__dict__['C']
except KeyError:
    pass
else:
    print(c)
    raise TestFailed("class not collected")

# verify that the reference to the function is gone
try:
    f = mod.__dict__['f']
except KeyError:
    pass
else:
    print(f)
    raise TestFailed("function not collected")
