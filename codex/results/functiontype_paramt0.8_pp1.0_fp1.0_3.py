from types import FunctionType
list(FunctionType(lambda: 'hello world', {})())

var = 'hello world'
def func():
    return var
list(func())

list('hello world')

[var for var in 'hello world']

var = 'hello world'
def func():
    return var
[var for var in func()]

var = 'hello world'
def func():
    return var
[char for char in var]

var = 'hello world'
def func():
    return var
[char.capitalize() for char in var]

var = 'hello world'
def func():
    return var
[char.capitalize() for char in func()]

var = 'hello world'
def func():
    return var
[char.capitalize() for char in func() if var[0] == 'h']

var = 'hello world'
def func(char):
    return char
[func(char) for char in func(var) if func(var[0]) == 'h']

var = 'hello world'
def func(char):
    return char
[func(
