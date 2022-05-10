import types
types.MethodType(new_func, obj)

# 给实例绑定的方法，对另一个实例是不起作用的
obj2 = Student()
# obj2.set_age(25)
