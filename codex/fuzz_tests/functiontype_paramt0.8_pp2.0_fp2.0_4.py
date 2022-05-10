from types import FunctionType
list(FunctionType(lambda x:x))

# parameters are separate from arguments
# parameters:
# we use parameters in function definition to create the function
# arguments:
# we use arguments in function call to pass values to the function
# different arguments can be passed to the same parameters when different calls are made

# def function_name(parameters):
#    """function documentation string"""
#    function body
#    return [expression]

# document string
# it is a string literal and it is available to us as the attribute of the function

def sayHello(name):
     "This prints a passed string on screen"
     print("Hello", name)
     return
# same as above
def sayHello2(name):
    """This prints a passed string on screen"""
    print("Hello", name)
    return

 # help() function will display the documentation string
help(print)
help(sayHello)
help(sayHello2)

print(sayHello.__doc__)
print(sayHello2.__doc__)
print(print.__doc__)

# the first statement of the function body can be an
