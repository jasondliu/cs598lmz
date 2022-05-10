from types import FunctionType
list(FunctionType(lambda: None))
# TypeError: 'list' object is not callable
list(FunctionType(lambda: None)())
# []

# Other collections:
class MyIterable:
    def __init__(self):
        self.items = [1, 2, 3]
    def __iter__(self):
        return iter(self.items)
list(MyIterable())
# [1, 2, 3]'

class MyDict:
    def __init__(self):
        self.items = {'key': 'value'}
    def __iter__(self):
        return iter(self.items)
dict(MyDict())
# {'key': 'value'}
