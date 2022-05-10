gi = (i for i in ())
# Test gi.gi_code.co_argcount
# Test gi.gi_frame.f_code.co_argcount

# Test iterating over a function with a for loop
def fd(self):
    return self

f = fd
for i in f:
    pass

# Test iterating over a function with a while loop
f = fd
i = 0
while i < 10:
    i += 1
    next(f)

# Test iterating over a function with a for loop
def gd(self, start):
    return gd

g = gd
for i in g:
    pass

# Test iterating over a function with a while loop
g = gd
i = 0
while i < 10:
    i += 1
    next(g)

# Test iterating over a function with a for loop
def hd(self, start, step):
    return hd

h = hd
for i in h:
    pass

# Test iterating over a function with a while loop
h = hd
i = 0
while i < 10:

