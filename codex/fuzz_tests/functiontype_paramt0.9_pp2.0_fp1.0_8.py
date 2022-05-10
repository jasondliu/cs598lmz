from types import FunctionType
list(FunctionType().__bases__)
[<class 'object'>]
>>> list(FunctionType().__bases__)[0].__bases__
()
>>> list(FunctionType().__bases__)[0].__bases__[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
```

## 多继承

一个类可以继承多个父类，在子类中同名方法将会调用第一个父类中定义的方法。

>同时子类也可以调用祖先类中的同名方法，这些规则将继续在子类中递归。


```Python
#!/usr/
