from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_freevars)

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'').__code__

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'').__code__.co_freevars

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'').__code__.co_freevars = ('a',)

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'').__code__.co_freevars = ('a',)

#%%
from types import CodeType
CodeType(
