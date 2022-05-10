from types import FunctionType
list(FunctionType(lambda x: False, globals(), "ret"))
# This fails with TypeError: init() takes exactly 1 argument (4 given)
</code>
Why is the constructor for <code>CodeType</code> provided with <code>4</code> arguments here?
The expected result here is a tuple containing a single falsy element.


A:

I'm assuming that you expect the first 4 arguments to the constructor to be:
<code>argcount, nlocals, stacksize, flags
</code>
In those days, the <code>CodeType</code> constructor expected not just a code object, but a whole series of parameters describing the code object.  So the <code>FunctionType</code> constructor itself filled in the first four parameters for you.
Here's the <code>opcode.opmap</code> from Python 1.5:
<code>&gt;&gt;&gt; from opcode import *
&gt;&gt;&gt; opmap
{'POP_TOP': 1, 'ROT_TWO': 2, 'ROT_THREE': 3, 'DUP_TOP':
