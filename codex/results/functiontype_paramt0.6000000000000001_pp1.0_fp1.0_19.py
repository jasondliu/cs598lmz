from types import FunctionType
list(FunctionType(f.__code__,globals()).__dict__.keys())

#%%
import math
math.sqrt(4)

#%%
#Exercise
#Write a function that takes a list of numbers as parameter.
#The function will return the sum of the list.
#If a string is passed in the parameter, the function will return the string 'Input is not a list'

#%%
def sum_func(numbers):
    if type(numbers) != list:
        return 'Input is not a list'
    else:
        return sum(numbers)

#%%
sum_func([1,2,3])

#%%
sum_func('this is a string')

#%%
#Exercise
#Write a function that takes a list of numbers as parameter.
#The function will return a list of the square root of each number in the input list.
#If a string is passed in the parameter, the function will return the string 'Input is not a list'.

#%%
def sqrt_func2(numbers):
    if type(numbers) !=
