import types
types.MethodType(my_add(3), m, Point) #instantiate "my_add" as a method

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
    def __add__(self, another):
        return Point(self.x + another.x, self.y + another.y)

class Point3D(Point):
    def __init__(self, x=0, y=0, z=0):
        super(Point3D, self).__init__(x, y)
        self.z = z
    def __str__(self):
        return '(%d, %d, %d)' % (self.x, self.y, self.z)
    def __add__(self, another):
        return Point3D(self.x + another.x, self.y + another.y, 
                       self.z + another
