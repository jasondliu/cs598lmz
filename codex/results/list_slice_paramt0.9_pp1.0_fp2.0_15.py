import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
print(bool(lst[0]))
del a
print(bool(lst[0]))
#禁止装饰器修改original_function的名字，否则inspect.stack()会跳帧
#利用functools和weakref让闭包拥有弱引用
def debug(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        args_repr=[repr(a) for a in args]
        kwargs_repr=['%s=%s'%(k,v) for k,v in kwargs.items()]
        signature='%s%s'%(func.__name__,repr(tuple(args_repr)+tuple(kwargs_repr)))
        print('calling %s'%signature)
        ret=func(*args,**kwargs)

