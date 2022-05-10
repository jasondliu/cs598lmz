import types
types.MethodType(f, None, Person)

# 给实例绑定一个方法
p = Person()
p.set_age = types.MethodType(f, p)
p.set_age(25)
p.age

# 给一个实例绑定的方法，对另一个实例是不起作用的
p2 = Person()
# p2.set_age(25)
