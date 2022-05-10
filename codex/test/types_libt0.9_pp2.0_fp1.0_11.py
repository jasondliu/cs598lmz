import types
types.MethodType(do_some.__func__, s)

# todo: 可见，应该用 setattr, setattr()函数可以用于任何实例，并且不管它具有哪些动态类型和特性，他都可以以相同的方式为其设置属性。
#
