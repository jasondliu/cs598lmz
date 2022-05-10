from types import FunctionType
list(FunctionType(lambda x, y: x+y, {}).__annotations__.items())[0]

"""
>>> list(FunctionType(lambda x, y: x+y, {}).__annotations__.items())[0]
('x', <class 'int'>)
>>> list(FunctionType(lambda x, y: x+y, {}).__annotations__.items())[1]
('y', <class 'int'>)
"""
