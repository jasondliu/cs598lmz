fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = "code.py"
# Test f.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1

# Test exception chaining
x1 = Exception("chained error 1")
x1.__cause__ = Exception("caused by")
x1.__cause__.__context__ = Exception("set context")
x2 = Exception("chained error 2")
x2.__context__ = x1
raise x2
