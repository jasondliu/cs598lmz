fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn.__code__.co_filename
fn.__code__.co_filename
# Test help function
help
# Test all the members of fn.__code__
[name for name in dir(fn.__code__) if not name.startswith('_')]
# Test the code_info class
from types import CodeType
from inspect import code_info

CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
code_info(fn)
# Test help_object
from inspect import help_obj
