from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, "foo", (), f.__defaults__, f.__closure__).__closure__)

# test_codeop
import codeop
codeop.compile_command("x = 1")
codeop.compile_command("x = 1", "<string>", "exec")
codeop.compile_command("x = 1", "<string>", "eval")
codeop.compile_command("x = 1", "<string>", "single")

# test_collections
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
p[0] + p[1]
x, y = p
x, y
p.x + p.y
p
d = p._asdict()
d['x']
Point(**d)
p._replace(x=100)

# test_collections_abc
from collections.abc import Sequence
isinstance([], Sequence)

# test_compileall
import compileall
comp
