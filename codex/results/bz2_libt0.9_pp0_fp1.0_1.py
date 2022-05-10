import bz2
bz2.decompress(sample)   

# After importing bz2 in the environment, the sample successfully decompressed!

 
# ---------------------------------
# Instructions (part 2-Implementing an error handler)
# ---------------------------------

# Assign the string 'This is the incorrect string to decompress.' to a variable incorrect_string.
# Write a try/except block to handle the possible exceptions that occur when attempting to decompress this string.

# _____________________________________

incorrect_string = 'This is the incorrect string to decompress.'
try:
    bz2.decompress(incorrect_string)
except :
    print("An exception occurred!")
  
# ---------------------------------
# Instructions (part 3-Raising an exception)
# ---------------------------------

# Decide which type of exception to raise.
# Write a raise statement to raise the exception you chose.

# _____________________________________

try:
    raise Exception("String Valued Exception")
except Exception as ex:
    print("An exception occurred!")
    print(ex.message)

# We chose the Exception class to raise, since it can hold
