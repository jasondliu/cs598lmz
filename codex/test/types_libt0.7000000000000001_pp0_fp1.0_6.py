import types
types.ClassType

# -------------------------------------
# 类的实例化
class Person:
    pass

xiaoming = Person()
xiaohong = Person()

xiaoming
xiaohong

# -------------------------------------
# 类的变量
class Person:
    name = 'Person'

p = Person()
print( p.name )

# -------------------------------------
# 实例变量
class Person:
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p1.name
p2.name

# -------------------------------------
# 类的方法
# 类的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种
