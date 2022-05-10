from types import FunctionType
list(FunctionType().__mro__)

## [<class 'type'>, <class 'object'>]

## this makes it possible to override the __init__ method in FunctionType.
## however, we cannot create an instance of FunctionType.

## this means we have to have a way to create a new FunctionType. that is what closures are
def make_adder(x):
    def g(y):
        return x + y
    return g

## a lambda has the form "lambda parameters: expression". Here we rewrite
## make_adder as a lambda.
def make_adder2(x):
    return (lambda y: x + y)

## the function
def make_adder3(x):
    def g(y):
        return x + y
    
## is equivalent to the lambda
def make_adder4(x):
    return (lambda y: x + y)

## Dictionaries
# Dictionaries are dynamic name-value pairs.
# There is no ordering on a dictionary.
eng2sp = {
    "one" : "uno"
    , "two" : "dos"
