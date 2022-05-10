from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'add1'))

# %%
from types import LambdaType
list(LambdaType(lambda x: x + 1, globals(), 'add1'))

# %%
from types import CodeType
list(CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b''))

# %%
from types import MappingProxyType
list(MappingProxyType({}))

# %%
from types import SimpleNamespace
list(SimpleNamespace())

# %%
from types import DynamicClassAttribute
list(DynamicClassAttribute())

# %%
from types import ModuleType
list(ModuleType('__main__'))

# %%
from types import TracebackType
list(TracebackType(None, None, None))

# %%
from types import FrameType
list(FrameType(None, None, None, None, None, None))

# %%
from types import GetSetDescriptorType
list(GetSetDescriptorType(None, None, None))

# %%

