import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
class C(list):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.append(1)
    def __getitem__(self, item):
        print('getitem')
        return super().__getitem__(item)
    def __setitem__(self, key, value):
        print('setitem')
        super().__setitem__(key,value)
    def __str__(self):
        return 'str'
    __repr__=__str__
if __name__ == '__main__':
    my_list=C([1,2,3])
    print(my_list)
    print(my_list[0])
    my_list[0]=2
    print(my_list)
    print(my_list[0])
    print(my_list.__class__)
    class MyClass:
        def __init__(self,foo=None):

