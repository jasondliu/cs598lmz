import gc, weakref

class Point(object):
    _ids = count()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = next(self._ids)

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class Line(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return 'Line({!r:},{!r:})'.format(self.start, self.end)

    def __str__(self):
        return '{}->{}'.format(self.start, self.end)

class Circle(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __re
