import types
types.MethodType(f, None, class1)

# 给实例绑定方法
class1.f = f
class1.f()

# 给实例绑定方法
class1().f()

# 给类绑定方法
class1.f = types.MethodType(f, class1)
class1.f()

# 给类绑定方法
class1().f()

# 给类绑定方法
class1.f = classmethod(f)
class1.f()

# 给类绑定方法
class1().f()

# 给类绑定方法
class1.f = staticmethod(f)
class1.f()

# 给类绑定方法
class1().f()

# 给类绑
