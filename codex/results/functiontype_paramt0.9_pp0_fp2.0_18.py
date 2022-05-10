from types import FunctionType
list(FunctionType(FunctionType.func_code(lambda x: x+x), FunctionType.func_globals(lambda x: x+x), FunctionType.func_name(lambda x: x+x), FunctionType.func_defaults(lambda x: x+x), FunctionType.func_closure(lambda x: x+x))(42))

# 2, A: [42], B: [42]
