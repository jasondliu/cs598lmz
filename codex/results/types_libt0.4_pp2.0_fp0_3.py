import types
types.MethodType(f, None, Person)

# 给一个实例绑定的方法，对另一个实例是不起作用的
p1 = Person()
p1.set_age(18)
p1.set_score(100)

p2 = Person()
p2.set_age(20)
p2.set_score(99)

# 给class绑定方法后，所有实例均可调用
Person.set_score(p1, 99)
p1.get_score()

# 使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Person实例添加name和age
