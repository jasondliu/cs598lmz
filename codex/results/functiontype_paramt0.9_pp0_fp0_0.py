from types import FunctionType
list(FunctionType(frame.f_code, frame.f_globals, "foo", (), None))
# TypeError: list() takes at most 1 argument (2 given)
</code>
What is the reasoning behind this, and can it be worked around, short of writing some wrapper function?
This is with Python 2.6.4.


A:

The above method for creating function objects is intended for a parser's use, as mentioned in the docs.
As a result, the signature of <code>FunctionType</code> will not likely change in the future.
We are back to the good old parsing our own functions, with <code>ast</code>:
<code>import ast
import sys
frame = sys.getframe(1)

source = open(frame.f_code.co_filename, 'r').read()
tree = ast.parse(source)
func = tree.body[frame.f_lineno - 3]
assert func.name == 'zzz'
</code>

