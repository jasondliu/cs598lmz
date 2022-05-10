import gc, weakref

#
#  This is the class that is used to create the object
#
class MyObj(object):
    def __init__(self, name):
        self.name = name
