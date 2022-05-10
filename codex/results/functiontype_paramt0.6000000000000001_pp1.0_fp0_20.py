from types import FunctionType
list(FunctionType(
    FunctionType(
        lambda: None, {}, '<lambda>', (), (), (), (), None, None),
    {}, '<lambda>', (), (), (), (), None, None
).__code__.co_freevars)

# TypeError: 'code' object is not subscriptable
# list(FunctionType(
#     FunctionType(
#         lambda: None, {}, '<lambda>', (), (), (), (), None, None),
#     {}, '<lambda>', (), (), (), (), None, None
# ).__code__.co_freevars)

# AttributeError: 'function' object has no attribute '__code__'
# list(FunctionType(
#     FunctionType(
#         lambda: None, {}, '<lambda>', (), (), (), (), None, None),
#     {}, '<lambda>', (), (), (), (), None, None
# ).__code__.co_freevars)

# AttributeError: 'function' object has no attribute '__code__'
# list(FunctionType(
#     FunctionType(
#         lambda: None
