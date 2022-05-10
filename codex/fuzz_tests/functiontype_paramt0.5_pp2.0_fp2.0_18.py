from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

#%%
def foo():
    a = 1
    b = 2
    c = 3

print(foo.__code__.co_varnames)
print(foo.__code__.co_argcount)

#%%
# Python的函数对象还有一些其他属性，但是基本上都是内部实现细节，
# 与这本书的主题无关，这里就不一一列举了。
# 但是有一个属性需要特别提一下，那就是__defaults__。
# 它是一个元组，里面保存着函数的默
