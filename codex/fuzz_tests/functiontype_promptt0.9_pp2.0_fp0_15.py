import types
# Test types.FunctionType
assert(type(test1) is types.FunctionType)
test1("Testing 1 2 3")

# Test types.BuiltinFunctionType
# assert(type(test2) is types.BuiltinFunctionType)
test2("Testing 1 2 3")

# Test types.TypeType
assert(type(A) is types.TypeType)
assert(type(A()) is A) # Note: A is a type, A() is an instance of that type
aInstance = A()
aInstance.print_msg("Instance of class A")
A.static_print_msg("Static method call")

my_list = list(("a", "b", "c")) # note the double round-brackets
print(my_list)

# Testing the str
# print(str(A))
aInstance.print_msg(str(type(aInstance)))
