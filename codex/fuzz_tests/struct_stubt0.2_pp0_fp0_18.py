from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# Descriptor
class Integer:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

class Point:
    x = Integer()
    y = Integer()

p = Point()
p.x = 10
p.y = 20
print(p.x, p.y)

# Metaclass
class Integer:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

class Point:
    x = Integer()
    y = Integer()

p = Point()
p.x = 10
p.y = 20
print(p.x, p.y)

# Metaclass
class Integer:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
