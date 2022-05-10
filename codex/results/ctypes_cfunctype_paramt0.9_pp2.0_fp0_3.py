import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p)

class Person():

    def __init__(self,firstName):
        self.firstName = firstName

    def say_hello(self):
        print("Hello %s"%(self.firstName))

class People(object):
    def __init__(self):
        self.people = {}

    def addPerson(self, fName, p):
        self.people[fName] = p

    def say_hi(self, fName):
        self.__getitem__(fName).say_hello()

    def __getitem__(self, fName):
        return self.peop
