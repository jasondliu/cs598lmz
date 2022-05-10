import gc, weakref, sys


class A(object):

    def __init__(self, message):
        self.message = message

    def __del__(self):
        print 'deleting', self.message, self.__class__.__name__


for i in range(5):
    a = a.write(message)
    del a

    gc.collect()
    print 'waiting to collect...'


class A(object):

    objects = weakref.WeakValueDictionary()

    def __init__(self, message):
        self.message = message
        self.objects[id(self)] = self


a1 = A('hello')

print a1.objects[id(a1)].message

A('world')

A('hello!')

print len(a1.objects)

a2 = A('world')

del a2

print len(a1.objects)

a1 = A('goodbye')

del a1

print len(a1.objects)

print 'A class has been destroyed'


class File
