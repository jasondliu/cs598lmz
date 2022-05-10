import gc, weakref

class Container(object):
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def get_objects(self):
        return self.objects

class Object(object):
    def __init__(self, name):
        self.name = name
        self.container = None

    def __repr__(self):
        return '&lt;Object %s&gt;' % self.name

