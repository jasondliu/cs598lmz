from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', (2))
print(s)
s.pack(0)
'''
'''
def hackoct(octs):
    if len(octs) != 3:
        raise ValueError
    if len(set(o for o in octs if not 0 <= o <= 255)) != 0:
        return ValueError

    def dot(a, b):
        return sum(a * b)
    return dot(octs, [256**2, 256, 1])
print(hackoct((21,152,213)))
'''
'''
class A():

    def foo(self, x):
        
        print ("executing foo(%s,%s)"%(self, x))

    @classmethod
    def class_foo(cls, x):
        print ("executing class_foo(%s,%s)"%(cls, x))

    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x)

a=A()
a.foo(4)

