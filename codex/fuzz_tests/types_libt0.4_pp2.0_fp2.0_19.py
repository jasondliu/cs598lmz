import types
types.MethodType(func, None, class_name)
```

```python
# 定义一个类
class Person(object):
    pass

# 定义一个函数
def set_age(self, age):
    self.age = age

# 给类动态绑定方法
Person.set_age = types.MethodType(set_age, Person)

# 创建一个对象
p = Person()
# 给对象动态绑定方法
p.set_age(25)
print(p.age)
```

<br>

## 使用元类

```python
# 定义一个类
class Person(object):
    pass

# 定义一个函数
def set_age(self, age):
    self.age = age

#
