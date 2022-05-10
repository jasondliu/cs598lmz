import ctypes
ctypes.cast(my_primes.ctypes.data, ctypes.POINTER(ctypes.c_int))

#używając biblioteki numpy
import numpy as np
np.ctypeslib.as_ctypes(my_primes)

#wykonywanie operacji na danych
#mapowanie
def prime_square_mapper(num):
    return num*num

def prime_square_mapper_ctypes(num):
    return ctypes.c_int(num.value * num.value)

#redukcja
def prime_square_reducer(num1, num2):
    return num1*num2
def prime_square_reducer_ctypes(num1, num2):
    return ctypes.c_int(num1.value * num2.value)

def prime_square_reducer_numpy(num1, num2):
    return num1*num2

#list comprehension
prime_squares = [prime_square_mapper(p) for p in my_
