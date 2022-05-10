import gc, weakref, inspect

class Object:

    def __init__(self, *args, **kwargs):
        pass

    def __del__(self, *args, **kwargs):
        pass

    def __repr__(self, *args, **kwargs):
        return "Object"

    def __eq__(self, *args, **kwargs):
        pass

    def __ne__(self, *args, **kwargs):
        pass

    def __hash__(self, *args, **kwargs):
        pass

class ReferenceCountingObject(Object):

    def __init__(self, *args, **kwargs):
        self.__dict__['_refcount'] = 1
        super(ReferenceCountingObject, self).__init__(*args, **kwargs)

    def __del__(self, *args, **kwargs):
        self.__dict__['_refcount'] = 0
        super(ReferenceCountingObject, self).__del__(*args, **kwargs)

