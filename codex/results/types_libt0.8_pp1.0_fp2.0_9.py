import types
types.MethodType
types.FunctionType

# 定义一个函数
def fn(self):
    return self.name + '123'
fn

# 动态给一个类增加方法
Student.saySomething = fn
s = Student('Hello')
s.saySomething()

## print (Student)
# 获取一个对象所有属性和方法
dir(s)

# getattr 可以获取对象属性和方法
getattr(s, 'height')
getattr(s, 'say')
getattr(s, 'say', 'not found')


# 给一个对象增加属性和方法
setattr(s, 'height', '150')
getattr(s, 'height')

setattr(s, 'go', fn)
s.
