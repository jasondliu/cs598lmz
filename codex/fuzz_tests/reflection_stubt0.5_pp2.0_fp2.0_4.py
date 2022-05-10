fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
TypeError: 'generator' object is not callable
```

## 结论

- `__code__`属性可以被设置成任何可调用对象;
- `__code__`属性可以被设置成`generator`对象;
- `__code__`属性被设置成`generator`对象后, 在调用时会报错;
