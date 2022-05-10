from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# function that returns a function
def my_func():
    def inner_func():
        return 'hello'
    return inner_func

my_func()

# named function
def my_func():
    def inner_func():
        return 'hello'
    return inner_func

my_func()

# named function
def my_func():
    def inner_func():
        return 'hello'
    return inner_func

my_func()()

# function that returns a function
def my_func():
    def inner_func():
        return 'hello'
    return inner_func

my_func()

# function that returns a function
def my_func():
    def inner_func():
        return 'hello'
    return inner_func

my_func()()

# function that returns a function
def my_func():
    def inner_func():
        return 'hello'
    return inner_func

func = my_func()
func()

# function
