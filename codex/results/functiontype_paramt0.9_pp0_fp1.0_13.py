from types import FunctionType
list(FunctionType([], lambda x: ''))
list(FunctionType.__call__)
list(FunctionType.__call__.__call__)
list(FunctionType.__call__.__call__.__call__)
list(FunctionType.__call__.__call__.__call__.__call__)

# Function bound method
list(FunctionType.__call__(lambda x: ''))

# Instance attribute
class C:
    def __init__(self):
        self.x = [[]] * 2
        self.y = [[], []]
list(C().x)
list(C().y)
