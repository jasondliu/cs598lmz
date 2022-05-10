from _struct import Struct
s = Struct.__new__(Struct)
print(s.format)

print(type(Struct.format))

# 我们在这里使用了两次 __new__ 方法，第一次用来创建类的实例，第二次用来创建绑定方法对象。
# 任何时候你都可以通过类调用 __new__ 方法来创建实例，但是你仅仅只能通过类调用 __new__ 方法
# 并且至少传入一个参数来创建绑定方法对象。
