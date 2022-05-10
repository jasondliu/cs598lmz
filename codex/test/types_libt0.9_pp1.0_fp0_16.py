import types
types.MethodType(new_add, d)

# 改变实例属性
Student.age = lambda self: 23
print(stu.age())
