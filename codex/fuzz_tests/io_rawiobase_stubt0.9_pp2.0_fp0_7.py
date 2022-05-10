import io
class File(io.RawIOBase):

    def __init__(self):
        ...

    def write(self, b):
        ...

    def readable(self):
        return True

#f = File()
#print(f.readable())
#f.read()


#Writing Decorators
#A decorator is a callable that takes another function as argument (the decorated function).
#The decorator may perform some processing with the decorated function,
#and returns it or replaces it with another function or callable object.

# decorator
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

# decorated
@uppercase
def greet():
    return 'Hello!'

#greet()
#'HELLO!'

#Start with a simple function that takes two arguments and returns their product.
#Add a decorator, using annotations, that multiplies the result of the function by 10.

# decorator
def mult_10(func):
    def by_10(a,b):

