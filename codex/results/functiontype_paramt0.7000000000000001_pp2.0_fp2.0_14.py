from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# Output:
# [<cell at 0x7f566be8caa0: function object at 0x7f566be8c848>,
#  <cell at 0x7f566be8cb78: int object at 0x7f566be8c7a0>]
```

Without the `inspect` module, we would have to do a lot of guesswork to access the closure data, or use the `dis` module to disassemble the bytecode.

The `getclosurevars` module does all the hard work for us.

```python
>>> from getclosurevars import getclosurevars
>>> closure_vars = getclosurevars(f)
>>> closure_vars.nonlocals
{'x': 1}
>>> closure_vars.globals
{'__name__': '__main__', '__doc__': None, 'x': 1, 'getclosurevars': <
