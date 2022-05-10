fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
# TypeError: 'generator' object is not callable
```

## `__code__`

```python
def fn():
    pass

fn.__code__
# <code object fn at 0x7f8c2d2d4420, file "<stdin>", line 1>

fn.__code__.co_varnames
# ('fn',)
```

## `__closure__`

```python
def fn():
    x = 1
    def fn2():
        print(x)
    return fn2

fn().__closure__
# (<cell at 0x7f8c2d2d4a88: int object at 0x7f8c2d3b3e60>,)

fn().__closure__[0].cell_contents
# 1
```

## `__globals__`

```python
def fn():
    pass

fn.__globals__
# {'__name__': '__main__', '__doc__': None
