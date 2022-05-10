from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# [<class 'type'>, <class 'object'>]
list(FunctionType(lambda x: x, globals(), "lambda").__mro__)

# <class 'function'>
type(FunctionType(lambda x: x, globals(), "lambda"))

# <class 'function'>
type(FunctionType(lambda x: x, globals(), "lambda").__call__)

# <class 'function'>
type(FunctionType(lambda x: x, globals(), "lambda").__call__.__call__)

# <class 'function'>
type(FunctionType(lambda x: x, globals(), "lambda").__call__.__call__.__call__)

# <class 'function'>
type(FunctionType(lambda x: x, globals(), "lambda").__call__.__call__.__call__.__call__)

# <class 'function'>
type(FunctionType(lambda x: x, globals(), "lambda").__call__.__call__.__call__.__call__.
