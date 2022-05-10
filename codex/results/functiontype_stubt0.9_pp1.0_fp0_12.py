from types import FunctionType
a = (x for x in [1])
print(type(a))  # 'generator', a 是生成器

# yield 
# list function 中有next()方法，str没有 next() 方法
# range() 也具有next()方法
# 凡是具有next() 方法的，都可以用for循环
# 那么是不是，所有具有next()方法的和generator可以转化
# 是
from functools import reduce
from functools import partial 
from functools import update_wrapper
from functools import WRAPPER_ASSIGNMENTS
from functools import WRAPPER_UPDATES
from collections import Iterator 
from collections import Iterable 
from collections import OrderedDict 
from collections import deque 
from traceback import format_tb 
from traceback import format_exception 

