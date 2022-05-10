gi = (i for i in ())
# Test gi.gi_code.co_freevars
# YIELD_VALUE should be a closure over the container of gi
gi.gi_code.co_freevars
# YIELD_VALUE should be a closure over the container of gi


# Test cell creation
c = (lambda: (yield))().gi_frame.f_locals['c']
c
# There should be no closure variables
c.cell_contents
c.cell_contents = 'abc'
c.cell_contents
# Check that it is really a cell
print(c)
# Check that it is really a cell
print(c.cell_contents)


# Test cell deletion
def f():
    del c

# Test that we cannot delete cells of the frame containing the cell
f.__code__.co_freevars
# Test that we can delete cells from the frame containing the code
def g():
    del d
d = (lambda: g()).__closure__[0]
g.__code__.co_freevars
g()


# Check that free variables are writable
def h():
   
