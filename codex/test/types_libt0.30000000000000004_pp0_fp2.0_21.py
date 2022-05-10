import types
types.MethodType(f,None,class_name)

#给一个实例绑定的方法，对另一个实例是不起作用的
s.set_age(25)
s.get_age()

s2 = Student()
s2.get_age()

#为了给所有实例都绑定方法，可以给class绑定方法
