from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for i in range(10))
# [<function foo at 0x7f1e3c0c5d08>, <function foo at 0x7f1e3c0c5d08>, <function foo at 0x7f1e3c0c5d08>, <function foo at 0x7f1e3c0c5d08>, <function foo at 0x7f1e3c0c5d08>, <function foo at 0x7f1e3c0c5d08>, <function foo at 0x7f1e3c0c5d08>, <function foo at 0x7f1e3c0c5d08>, <function foo at 0x7f1e3c0c5d08>, <function foo at 0x7f1e3c0c5d08>]

# a function is a closure
# a closure is a function
# a function is a closure
# a closure is a function
# a function is a closure
# a closure is a function
# a function is a closure
# a closure is
