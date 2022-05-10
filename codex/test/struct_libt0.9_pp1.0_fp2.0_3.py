import _struct
import types

class Py4JError(Exception):
    pass

class Py4JNetworkError(Py4JError):
    pass

class Py4JJavaError(Py4JError):
    
    def __init__(self, java_exception):
        self.java_exception = java_exception
    
    def __str__(self):
        if self.java_exception is not None:
            return "<Java Exception=%s>" % (self.java_exception)
        else:
            return "<Java Exception>"

class BaseError(Py4JError):
    pass

class Py4JIncorrectArgumentCountError(BaseError):
    
    def __init__(self, name, given, expected):
        self.name = name
        self.given = given
        self.expected = expected
        
    def __str__(self):
        return "%s: incorrect number of arguments given (%d) for %d" %\
            (self.name, self.given, self.expected)

