from types import FunctionType
list(FunctionType(lambda x: x + 1, globals())(1))

# %%
from types import LambdaType
list(LambdaType(lambda x: x + 1, globals(), '<lambda>')(1))

# %%
from types import GeneratorType
list(GeneratorType(lambda x: x + 1, globals(), '<lambda>', (), None))

# %%
from types import CodeType
CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# %%
from types import MappingProxyType
MappingProxyType({})

# %%
from types import SimpleNamespace
SimpleNamespace()

# %%
from types import DynamicClassAttribute
DynamicClassAttribute()

# %%
from types import _GeneratorWrapper
_GeneratorWrapper(lambda x: x + 1, globals(), '<lambda>', (), None)

# %%
from types import _CoroutineWrapper
_CoroutineWrapper(lambda x: x + 1, globals(), '<lambda>', (), None)

# %%
