import types
types.MethodType(func,None,Foo)

# 2, 类的实例对象
f = Foo()
f.func = types.MethodType(func,f)
f.func()

# 3, 直接用类名去调用
Foo.func = types.MethodType(func,None,Foo)
Foo.func()

# 对于非绑定方法来说,无论是类还是实例都可以去调用
Foo.func()
f.func()

# 对于绑定方法来说,只能由实例去调用
f.func()
