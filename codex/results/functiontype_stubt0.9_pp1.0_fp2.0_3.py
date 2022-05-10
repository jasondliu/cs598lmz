from types import FunctionType
a = (x for x in [1])
b = 1

isinstance(a, GeneratorType)

isinstance(b, int)

isinstance(b, float)

isinstance(b, object)

isinstance(b, int)

isinstance(b, FunctionType)

def func():
    pass


isinstance(b, (float, int))

isinstance(2.2, (float, int))

# %%
"""
仍然用shelve模块来做例子，假设如果db变量被定义为shelve.open('shelve_test.db')
"""
# %%
shelve.open('shelve_test.db')

# %%
getattr(db, 'close')

setattr(db, 'c', 'python')

hasattr(db, 'c')

# %%
"""
重构时，使用getattr和hasattr可以
