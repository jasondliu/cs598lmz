import gc, weakref
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(10) # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a # does not create a reference
print d['primary'] # fetch the object if it is still alive

del a # remove the one reference
gc.collect() # run garbage collection right away

print d['primary'] # entry was automatically removed

#===============================================================================
# from pprint import pprint
# import weakref
# class Cheese:
#     def __init__(self, kind):
#         self.kind = kind
#     def __repr__(self):
#         return 'Cheese(%r)' % self.kind
# stock = weakref.WeakValueDictionary()
# catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
#             Cheese('Brie'), Cheese('Parmesan')]
# for cheese in catalog:
#     stock[cheese.kind] =
