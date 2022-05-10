fn = lambda: None
# Test fn.__code__.co_flags
try:
    fn.__code__.co_flags
except AttributeError:
    def flags(x):
        return 0
else:
    def flags(x):
        return x.__code__.co_flags
# Test fn.__code__.co_varnames
try:
    fn.__code__.co_varnames
except AttributeError:
    def varnames(x):
        return None
else:
    def varnames(x):
        return x.__code__.co_varnames
# Test fn.func_globals
try:
    fn.func_globals
except AttributeError:
    def globals(x):
        return None
else:
    def globals(x):
        return x.func_globals
# Test fn.func_code
try:
    fn.func_code
except AttributeError:
    def code(x):
        return None
else:
    def code(x):
        return x.func_code

if hasattr(__builtins__,
