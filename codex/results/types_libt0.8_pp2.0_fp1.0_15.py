import types
types.MethodType(fn, obj_1)

def fn(self):
    print('self is obj_2')
obj_2.f = fn

# 这是一个类的实例方法，只能由实例调用
obj_1.f()
obj_2.f()

# 这是一个类的实例方法，只能由实例调用
Student.f(obj_1)

# 这是一个类的静态方法，可以由实例调用
Student.static_f()
