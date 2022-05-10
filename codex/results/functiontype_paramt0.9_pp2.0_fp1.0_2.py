from types import FunctionType
list(FunctionType(lambda: None, globals(), '<lambda>').__code__.co_varnames)

# P EP 572即将于2020年出现。它允许代码的变量和属性访问它们的名称。
# 使用嵌入的名称引用代码变量名 :嵌入的名称引用代码变量名称。
# （__name__）由 > = 3.7的Python实现，基于PEP 526
x = 10
y = 20
f = lambda: x + y
f'{f.__name__}(x, y) = {f.__code__.co_varnames}'

f.__name__

f.__code__.co_varnames
#
#

import p
