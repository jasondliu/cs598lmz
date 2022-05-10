gi = (i for i in ())
# Test gi.gi_code is NULL.
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print("FAILED: gi.gi_code is not NULL")

# Create closure.
def f():
    def g():
        return 42
    return g
g = f()
# Test g.__closure__ is set.
if g.__closure__ is None:
    print("FAILED: g.__closure__ is NULL")
# Test g.func_closure is set.
if g.func_closure is None:
    print("FAILED: g.func_closure is NULL")
# Test closure cell contents.
if g.__closure__[0].cell_contents != 42:
    print("FAILED: g.__closure__[0].cell_contents is incorrect")
if g.func_closure[0].cell_contents != 42:
    print("FAILED: g.func_closure[0].cell_contents is incorrect")

# Create closure.
def f():
    x = 42
    def g():
       
