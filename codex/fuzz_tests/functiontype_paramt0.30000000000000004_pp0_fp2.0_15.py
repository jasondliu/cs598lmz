from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'lambda')(2))

# %%
from types import LambdaType
list(LambdaType(lambda x: x + 1, globals(), 'lambda')(2))

# %%
from types import CodeType
list(CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')(2))

# %%
from types import MappingProxyType
list(MappingProxyType({1: 2}).items())

# %%
from types import SimpleNamespace
list(SimpleNamespace(x=1).x)

# %%
from types import ModuleType
list(ModuleType('a').__name__)

# %%
from types import DynamicClassAttribute
list(DynamicClassAttribute)

# %%
from types import TracebackType
list(TracebackType)

# %%
from types import FrameType
list(FrameType)

# %%
from types import GetSetDescriptorType
list(GetSetDescriptorType)

# %%
from types import MemberDescriptorType
