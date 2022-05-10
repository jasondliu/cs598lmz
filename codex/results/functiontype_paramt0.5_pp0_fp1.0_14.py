from types import FunctionType
list(FunctionType(f.__code__,f.__globals__,name = 'f',argdefs = (1,),closure = ()))

# 测试lambda表达式
func = lambda x:x+1
print(func(3))
print(type(func))
print(func.__name__)
print(func.__closure__)
print(func.__code__)
print(func.__code__.co_code)
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)
print(func.__code__.co_flags)

# 测试类方法
class C:
    def f(self):
        return self.x
c = C()
c.x = 1
print(c.f())
print(type(c.f))
print(c.f.__name__)
print(c.f.__closure__)
print(c.f.__code__)
print(c.f.__code__.co
