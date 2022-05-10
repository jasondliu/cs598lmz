fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__call__()
 
Code对象，对应字节码对象，所有的函数在被调用时，先将其解释为字节码对象，然后再执行
字节码的编译，可以用dis模块来进行反编译。
>>> def func(name):
...     print('hello', name)
...
>>> func('Tom')
hello Tom
>>> from dis import dis
>>> dis(func)
  2           0 LOAD_CONST               1 ('hello')
              2 LOAD_FAST                0 (name)
              4 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10
