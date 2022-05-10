import types
types.MethodType(foo, None, None)
# => <bound method types.MethodType.foo of NoneType object at 0x2b1b542c7048>
```

#### 7

```py
def foo():
    pass

dis.code_info(foo)
# => CodeInfo(stacksize=2, flags=67, locals={'foo': [], 'kwargs': []}, args=None, varargs=0, varkwargs=1, filename='<stdin>', name='foo', argcount=0)
```

#### 8

```py
import dis
dis.disco(None)
# => File "<stdin>", line 1
#    dis.disco(None)
#       ^
# SyntaxError: invalid syntax
```

#### 9

```py
def foo(x):
    pass

foo.__closure__
# => (None, None)
```

#### 10

```py
def foo(x):
    def bar():
        pass
    return bar

foo.__
