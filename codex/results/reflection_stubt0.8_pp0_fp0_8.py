fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
```

```
>>> fn()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not callable
```

只有在用`fn.__code__` = `code`的时候，`code`才会被解释器认为是生成器

```
>>> f = (i for i in ())
>>> f.__code__ = None
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not callable
```

### `__closure__`

在做编译的时候，用`ast.parse`解析出`AST`，然后调用`compile`编译，生
