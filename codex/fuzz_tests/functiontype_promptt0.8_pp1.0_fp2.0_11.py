import types
# Test types.FunctionType
# Instantiate FunctionType
def a_function( ): pass
a_function_type = types.FunctionType( a_function.__code__, globals( ), a_function.__name__, a_function.__defaults__, a_function.__closure__ )
# Instantiate FunctionType with nested FunctionType default argument
def b_function( ): pass
def a_function( x = b_function ): pass
a_function_type = types.FunctionType( a_function.__code__, globals( ), a_function.__name__, a_function.__defaults__, a_function.__closure__ )

# Test types.CodeType
# Instantiate CodeType
code_type_type = types.CodeType( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 )
