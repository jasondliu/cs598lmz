import _struct
import array

class Vec2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Vec2(%s, %s)" % (self.x, self.y)

class Vec3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "Vec3(%s, %s, %s)" % (self.x, self.y, self.z)

class Vec4(object):
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
