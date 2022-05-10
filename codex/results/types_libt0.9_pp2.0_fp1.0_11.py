import types
types.MethodType(do_some.__func__, s)

# todo: 可见，应该用 setattr, setattr()函数可以用于任何实例，并且不管它具有哪些动态类型和特性，他都可以以相同的方式为其设置属性。
#
# 5. dir()
# Python 最不需要说明的函数是 dir()，直接查看 Python 对象.
# dir() 不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参
