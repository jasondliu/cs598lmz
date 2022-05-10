import types
types.ModuleType.__repr__ = lambda self: self.__name__

# This is needed because otherwise the module name is interpreted as a
# callable object and the value of __name__ is used as the first
# argument, which in our case is the string "self".
types.ModuleType.__str__ = lambda self: self.__name__

# TODO: See the following for alternative approaches:
# http://code.activestate.com/recipes/576993-pretty-print-module-names-in-ipython/
# http://snipplr.com/view/33207/pretty-print-module-names-in-ipython/
# http://stackoverflow.com/questions/152356/whats-the-pythonic-way-to-use-getters-and-setters/160848#160848
# http://stackoverflow.com/questions/12686918/why-does-ipython-not-show-the-full-module-path-when-displaying-objects
