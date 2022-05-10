from types import FunctionType
list(FunctionType(f.__code__, globals(), "f"))

# %%
from types import MappingProxyType
d = {1: "A"}
d_proxy = MappingProxyType(d)
d_proxy

# %%
d_proxy[1]

# %%
d_proxy[2] = "x"

# %%
d_proxy

# %%
d[2] = "B"
d_proxy

# %%
from types import SimpleNamespace
data = SimpleNamespace(color="red", value=42)
data.color

# %%
data.value

# %%
from types import ModuleType
math = ModuleType("math")
math.pi = 3.14159
math.pi

# %%
import math
math.pi

# %%
math.tau = 2 * math.pi
math.tau

# %%
import sys
math

# %%
from types import DynamicClassAttribute
class A:
    def foo(self):
        return 42
    bar = DynamicClassAttribute(foo)

# %%
A().bar


