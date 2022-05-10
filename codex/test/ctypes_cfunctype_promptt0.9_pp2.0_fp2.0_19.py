import ctypes
# Test ctypes.CFUNCTYPE function, a function as a variable in python - 2_5.c
# In 2_5.c, the program includes a function called void print_function(void(*function)()), which takes a function as the argument and then calls that function. 
# Write a C program, 2_5.py that imports ctypes and creates a function using CFUNCTYPE. 
# The function should print out a message and then return. 
# Pass that function to your print_function function in 2_5.c as the argument and call the print_function function.

# This is 2_5.c
# #include <stdio.h>

# void print_function(void (*function)());

# void print_five()
# {
#     puts("Hello, five!");
# }

# int main()
# {
#     print_function(print_five);
#     return 0;
# }


def print_five():
    print("Hello, five!")

# CMPFUNC(restype, *argtypes, use_errno=False, use_last_error=
