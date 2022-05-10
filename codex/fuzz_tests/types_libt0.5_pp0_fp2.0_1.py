import types
types.MethodType(my_function, obj)

# 类似__slots__这种形如__xxx__的变量在Python中是有特殊用途的，
# 可以被直接访问，不是private变量，所以，不能用__name__、__score__这样的变量名。

# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你
