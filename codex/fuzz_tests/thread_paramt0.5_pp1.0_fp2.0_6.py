import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello, world\n")).start()
# hello, world

# The lambda function can have any number of arguments but only one expression.
# It cannot contain any statements and it returns a function object which can be assigned to any variable.
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Use lambda functions when an anonymous function is required for a short period of time.
# A lambda function that adds 10 to the number passed in as an argument and print the result:
x = lambda a : a + 10
print(x(5))
# 15

# A lambda function that multiplies argument a with argument b and print the result:
x = lambda a, b : a * b
print(x(5, 6))
# 30

# A lambda function that sums argument a, b, and c and print the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
# 13

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous
