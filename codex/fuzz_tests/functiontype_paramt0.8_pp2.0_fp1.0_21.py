from types import FunctionType
list(FunctionType(lambda: "test").__code__.co_varnames)

# so we can do this ...
list(varnames_of(lambda: "test"))

# ... or this
from lambda_functions import varnames_from_args
varnames_from_args(["a", "b", "c"])

# ... or even this
def varnames_from_args_and_kwargs(args, kwargs):
    kwarg_keys = list(kwargs.keys())
    return varnames_from_args(args) + kwarg_keys

varnames_from_args_and_kwargs(["a", "b", "c"], {"d": "e"})

# This is cool and all, but what about the lambda function's body?
# What if we want to execute it? For that, we need to generate code ...
from lambda_functions import code_from_body

code_from_body('return "test"')

# This is a byte-string, but we can move it into a namespace like so:

from lambda_
