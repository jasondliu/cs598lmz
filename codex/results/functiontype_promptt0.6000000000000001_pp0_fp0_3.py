import types
# Test types.FunctionType and types.LambdaType

# Lambda function definition:
add = lambda x,y: x+y

# Using the types module:
if type(add) == types.LambdaType:
    print("add is a lambda function")
else:
    print("add is not a lambda function")

# Using the isinstance() function:
if isinstance(add, types.LambdaType):
    print("add is a lambda function")
else:
    print("add is not a lambda function")

# Using the __name__ attribute:
if add.__name__ == '<lambda>':
    print("add is a lambda function")
else:
    print("add is not a lambda function")


# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total


# Now you can call sum function
total = sum( 10, 20 )
print("Outside the function : ", total )

def changeme( mylist
