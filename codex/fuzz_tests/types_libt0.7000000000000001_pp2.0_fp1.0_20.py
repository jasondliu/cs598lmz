import types
types.MethodType(func,obj)

# 为对象绑定一个方法
obj.fun = types.MethodType(func,obj)
obj.fun()
```

```python
class Student(object):
    def __init__(self,name):
        self.name = name

    def set_func(self,func,*args):
        self.func = types.MethodType(func,self,Student)
        self.args = args

    def call_func(self):
        return self.func(*self.args)

def func(self,x,y):
    return self.name + str(x + y)

s = Student('tarena')
s.set_func(func,1,2)
print(s.call_func())
```

###### 2.类方法

```python
class Student(object):

    def __init__(self,name):
        self.name = name

    def call(self,*args):
        return Student.func(*
