import bz2
bz2.decompress(compressed_data)

'''


##########  Exceptions ##############

'''
print("Starting")
try:
    # raise ValueError("This is a generated error")
    raise OverflowError("Math error")
# This will print error messages of the defined type
except OverflowError as e:
    # This will ignore the error
    pass
except ValueError as e:
    print("The error is: ", e)
# Note the else does not work the same way as in a for loop
else:
    print("This code block will only run if there are no errors")
finally:
    print("This code block is always executed")
print("Finishing")

# To test when things are working well
try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    pass
else:
    print("This code will only run if there are no errors")
finally:
    print("This code block is always executed")

# Defining my own exceptions
class DateError(ValueError):
   
