from types import FunctionType
list(FunctionType(f.__code__, f.__globals__).__closure__)

f.__closure__

import inspect
inspect.isclosure(f)

inspect.getclosurevars(f)

# %%

class A:
    pass

class B:
    pass

class C(A, B):
    pass

C.__bases__

# %%

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

D.__bases__

D.mro()

# %%

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

D.__mro__

# %%

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

D.mro()

#
