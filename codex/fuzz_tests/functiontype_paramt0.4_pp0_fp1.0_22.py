from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda') for _ in range(5))

# %%
# Получаем все функции из модуля
import math
[func for func in dir(math) if isinstance(getattr(math, func), FunctionType)]

# %%
# Получаем все переменные из модуля
import math
[var for var in dir(math) if not isinstance(getattr(math, var), FunctionType)]

# %%
# Создаем переменную из строки
a = 'variable'
b = globals()[a] = 'value'
b

# %%
# Создаем переменную из строки
a = 'variable
