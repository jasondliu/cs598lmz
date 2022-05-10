import ctypes
ctypes.cast(0x12345678, ctypes.c_void_p).value

#1. Create a function called division. It 
#   should accept two parameters, numerator 
#   and denominator, and return the result of 
#   numerator / denominator.

#2. Modify the division function so that if the 
#   denominator is zero, it returns zero instead 
#   of exiting the program.

#3. Modify the division function so that if the 
#   numerator is zero, it prints "not possible" 
#   to the console and returns zero instead of 
#   exiting the program.

#4. Modify the division function so that it 
#   prints "division by zero" to the console if 
#   the denominator is zero, and it returns zero 
#   instead of exiting the program.
