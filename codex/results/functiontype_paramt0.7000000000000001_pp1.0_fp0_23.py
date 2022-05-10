from types import FunctionType
list(FunctionType(function))

###############################################################################
# a function is an class
class MyFunction(object):
    def __init__(self, function):
        self.function = function

myfunction = MyFunction(function)
myfunction.function

###############################################################################
# a function is an object
function.__class__

###############################################################################
# a functi
