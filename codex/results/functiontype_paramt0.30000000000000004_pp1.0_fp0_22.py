from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'').__code__

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'').__code__.co_varnames

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'').__code__.co_varnames[0]

#%%
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'').__code__.co_varnames[0] = 'spam'

#%%
from types import CodeType
CodeType
