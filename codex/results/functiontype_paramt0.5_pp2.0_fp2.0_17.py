from types import FunctionType
list(FunctionType(lambda: print('hello'), globals()))

# <codecell>

import inspect
inspect.getcallargs(lambda: print('hello'))

# <codecell>

import inspect
inspect.getcallargs(lambda: print('hello'), 'hello')

# <codecell>

def f(x, y=2):
    return x + y

# <codecell>

inspect.getcallargs(f, 1)

# <codecell>

inspect.getcallargs(f, 1, y=1)

# <codecell>

inspect.getcallargs(f, 1, 2)

# <codecell>

inspect.getcallargs(f, 1, 2, 3)

# <codecell>

inspect.getcallargs(f, 1, 2, 3, 4)

# <codecell>

inspect.getcallargs(lambda x, y=2: x + y, 1)

# <codecell>

inspect.getcallargs(lambda x, y=2
