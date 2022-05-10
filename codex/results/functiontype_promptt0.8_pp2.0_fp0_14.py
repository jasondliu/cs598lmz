import types
# Test types.FunctionType

message = "Everything went well"

def print_message(msg):
    print(msg)

print_message(message)
print_message(type(print_message))
print_message(type(type))
print_message(types.FunctionType)

# print_message(types.FunctionType(print_message))
fprint = types.FunctionType(print_message.__code__, globals(), print_message.__name__, print_message.__defaults__, print_message.__closure__)
print_message(type(fprint))
fprint(message)
print(fprint)
print(print_message)
