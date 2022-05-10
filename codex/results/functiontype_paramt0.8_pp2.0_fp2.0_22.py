from types import FunctionType
list(FunctionType(lambda x: abs(x), globals()) for _ in range(10))
</code>
I tried to fix it this way:
<code>from types import FunctionType
from types import LambdaType
# global &lt;function abs at 0x7f1c7d9728c8&gt;
# globs = {abs.__name__: abs}
# globs = {abs.__name__: abs.__code__}
# globs = {abs.__name__: abs.__code__}
globs = {abs.__name__: abs.__code__.co_consts[0]}
globs = {abs.__name__: abs.__code__.co_consts[1]}
globs = {abs.__name__: abs.__code__.co_consts[1].__code__}
globs = {abs.__name__: abs.__code__.co_consts[1].__code__.co_consts[0]}
# globs = {abs.__name__: abs.__code__.co_consts[1
