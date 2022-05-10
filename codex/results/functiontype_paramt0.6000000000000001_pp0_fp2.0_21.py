from types import FunctionType
list(FunctionType(f1, globals(), 'f2'))
# [1, 2, 3]
```

## \_\_code\_\_

```python
def f():
    pass

f.__code__
# <code object f at 0x7f2158b3f780, file "<ipython-input-1-e7e9edc6d9d6>", line 1>

f.__code__.co_name
# 'f'

f.__code__.co_argcount
# 0

f.__code__.co_varnames
# ()

f.__code__.co_filename
# '/home/ubuntu/work/python/python-note/python-func.ipynb'

f.__code__.co_firstlineno
# 1
```

## \_\_closure\_\_

```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

make_adder(1)
# <function __main
