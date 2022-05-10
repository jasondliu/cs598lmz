from types import FunctionType
list(FunctionType(x, globals(), 'lambda_function_name') for x in (lambda_function.__code__.co_consts))
</code>
But that is also not working.
How do i get the list of all the lambda functions in the code?


A:

You can find all the lambda functions in your code, including the ones in your nested functions, with the following code:
<code>import dis

def find_lambdas(bytecode):
    """Find all the lambdas in a bytecode object"""
    for instruction in bytecode:
        if instruction.opname == "LOAD_LAMBDA":
            yield instruction.argval
        elif instruction.opname == "MAKE_FUNCTION":
            yield from find_lambdas(instruction.argval)

def find_lambdas_in_code(code):
    """Find all the lambdas in a code object"""
    for const in code.co_consts:
        if isinstance(const, type(code)):
            yield from find_lambdas_in_code(const)

