from types import FunctionType
list(FunctionType(filter(lambda el: el.kind == dis.INSTR,
                          dis.get_instructions(filter)),
                   globals(), 'add_one')
      .__code__.co_consts)

# [<code object <lambda> object at 0x7f1193fcb0e0>, 1, '<genexpr>', None]
[c for c in filter.__code__.co_consts if isinstance(c, type(filter.__code__))]

# [<code object filter at 0x7f1193f3c0e0, file "<ipython-input-9-2d8918e8e2a0>", line 1>]
```
