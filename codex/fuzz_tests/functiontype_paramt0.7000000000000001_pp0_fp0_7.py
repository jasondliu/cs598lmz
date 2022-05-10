from types import FunctionType
list(FunctionType(x))
 
# <codecell>

x.__code__.co_code
 
# <codecell>

x.__code__.co_consts
 
# <codecell>

x.__code__.co_names
 
# <codecell>

x.__code__.co_stacksize
 
# <codecell>

x.__code__.co_varnames
 
# <codecell>

import dis
dis.dis(x)

# <codecell>

# that's enough for now
 
# <codecell>



# <codecell>

# Class definitions

# <codecell>

# Example class

# <codecell>

class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def foo(self):
        return self.x * self.y

# <codecell>

a = A(1,2)
a.foo()
 
# <codecell>
