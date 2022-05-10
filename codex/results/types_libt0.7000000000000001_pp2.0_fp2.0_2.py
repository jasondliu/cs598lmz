import types
types.MethodType(lambda self: self.x, None, Derived)

# TypeError:
#   python3: cannot create 'builtin_function_or_method' instance
#   python2: cannot create 'instancemethod' instance
#
# 不管是python2还是python3，直接绑定一个函数到类上都是可以的。

# 在绑定函数之前，先把这个类的__dict__输出一下
# 这时可以看到这个类上有一个__dict__
print(Derived.__dict__)

# 在绑定之后，再次输出这个类的__dict__
Derived.__dict__['f'] = types.MethodType(lambda self: self.x, None, Der
