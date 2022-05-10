from _struct import Struct
s = Struct.__new__(Struct)
print(s)


# Example 2
class Struct:
    def __init__(self, format, *args):
        self.format = format
        self.size = Struct.calcsize(format)
        self.data = Struct.pack(format, *args)

    def pack(self, format, *args):
        pass

    def unpack(self, data):
        pass

    def unpack_from(self, data, offset=0):
        pass

    def calcsize(self):
        pass


"""
Note:

1. The __new__ method always returns the instance of the class.

2. __new__ method is called before the __init__ method.

3. __new__ method should return an instance of the class (same class in which it is defined).

4. __init__ method can modify the attributes of the class.

5. __new__ method can modify the attributes of the class.

6. __new__ method can return any other instance of the class.

7. __new__ method can return any other object which is then returned by the
