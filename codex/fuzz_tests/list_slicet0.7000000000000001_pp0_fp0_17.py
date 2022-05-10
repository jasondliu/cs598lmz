import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

'''

class MyClass:
    def __init__(self):
        self.x = 0

    def increment(self):
        self.x += 1

    def __del__(self):
        print('__del__ is called')


if __name__ == '__main__':
    o = MyClass()
    o.increment()
    w = weakref.ref(o)
    print(w)
    print(w().x)
    o.increment()
    print(w().x)
    del o
    print(w().x)
