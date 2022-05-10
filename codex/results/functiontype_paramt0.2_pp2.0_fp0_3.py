from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__qualname__', '__annotations__', '__closure__', '__code__', '__defaults__', '__dict__', '__doc__', '__globals__', '__kwdefaults__', '__module__', '__name__', '__self__', '__get__', '__call__', '__new__', '__init__', '__prepare__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# https://stackoverflow.com/questions/1534210/get-list-of-all-attributes-and-methods-of-an-object
# https://stackoverflow.com/questions/1389180/python-automatically-initialize-instance-variables
# https://stackoverflow.com/questions/423533/how-do-i-get-a-list-of
