import gc, weakref

class First(object):
    def __init__(self):
        self.s = 'text'
        self.calc = lambda x: x * 3

class Second(object):
    def __init__(self):
        self.s = 'text2'
        self.calc = lambda x: x ** 2
