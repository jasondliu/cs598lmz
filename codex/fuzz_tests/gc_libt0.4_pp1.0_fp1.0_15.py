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

    def __del__(self):
        print 'Deleting %s' % self
        if self.container is not None:
            self.container.remove_object(self)

if __name__ == '__main__':
    container = Container()
    obj1 = Object('obj1')
    obj2 = Object('obj2')
    container.add_object(obj1)
    container.add_object(obj2)
    print container.get_objects()
    del
