import weakref

class Foo(object):

    def __init__(self, name):
        self.name = name
        print('created {}'.format(self.name))

    def __del__(self):
        print('deleted {}'.format(self.name))

f1 = Foo('f1')
f2 = f1

# f1 -> f2 

#f1 = None
#f2 = None

del f1

# f2 -> f1

del f2

f3 = Foo('f3')
wd = weakref.ref(f3)

del f3
print(wd())
