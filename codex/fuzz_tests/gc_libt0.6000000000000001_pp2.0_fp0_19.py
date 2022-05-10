import gc, weakref
import sys, traceback

class Object(object):
    def __init__(self):
        self.__dict__["_Object__observers"] = []

    def __setattr__(self, name, value):
        if name[0] != "_":
            self.notify(name, value)
        self.__dict__[name] = value

    def notify(self, name, value):
        for observer in self.__observers:
            observer.notify(name, value)

    def addObserver(self, observer):
        if not observer in self.__observers:
            self.__observers.append(observer)

    def removeObserver(self, observer):
        if observer in self.__observers:
            self.__observers.remove(observer)

class Observer(object):
    def __init__(self, subject, *attrs):
        self.__state = {}
        self.__subject = subject
        self.__attrs = attrs
        self.__subject.addObserver(self
