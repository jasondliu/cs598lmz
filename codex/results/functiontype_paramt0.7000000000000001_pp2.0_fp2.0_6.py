from types import FunctionType
list(FunctionType('string', globals(), 'return 1'))
```

##### 2.4.4.4 可变参数

* 支持 *args 可变参数 **kwargs 可变参数
* 可变参数支持字符串、列表、字典
* 字典可变参数的值不可变，不支持指定字典的值为可变参数
* 不支持含有 *args 可变参数的可变参数，例如 `def test(*args, **kwargs)`
* 可变参数的参数名不能和函数的其他参数名相同

####
