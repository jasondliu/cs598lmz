from types import FunctionType
list(FunctionType(lambda: None, globals(), "") for _ in range(100))
# [<function <lambda> at 0x7f62f560c730>,
#  <function <lambda> at 0x7f62f560c7b8>,
#  <function <lambda> at 0x7f62f560c840>,
#  <function <lambda> at 0x7f62f560c8c8>,
#  <function <lambda> at 0x7f62f560c950>,
#  <function <lambda> at 0x7f62f560c9d8>,
#  <function <lambda> at 0x7f62f560ca60>,
#  <function <lambda> at 0x7f62f560cae8>,
#  <function <lambda> at 0x7f62f560cb70>,
#  <function <lambda> at 0x7f62f560cbf8>,
#  <function <lambda> at 0x7f62f560cc80>,
#  <function <lambda> at 0x7f62f560cd08>,
# 
