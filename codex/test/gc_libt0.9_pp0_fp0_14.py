import gc, weakref, sys


class A(object):

    def __init__(self, message):
        self.message = message

