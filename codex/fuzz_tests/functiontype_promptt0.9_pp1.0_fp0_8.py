import types
# Test types.FunctionType to know when to use or not eval
# isinstance(function_name, types.FunctionType)
def print_one(arg1):
    print "arg1: %r" % arg1

def print_two(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_none():
    print "I got nothing."

print_one("First!")
print_two("Zed", "Shaw")
print_none()
