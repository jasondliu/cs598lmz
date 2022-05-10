import codecs
codecs.register_error("strict", codecs.ignore_errors)
import random
import logging

# 2.2
## 判断是否是字符串
# isinstance("a", basestring)
# 
# 2.3
## 判断是否是数字
# isinstance("a", Number)
# type("a") == type(1)
# 
# 2.4
# 判断是否是整数
# isinstance("a", IntType)
# type("a") == type(1)
# 判断是否是浮点数
# isinstance("a", FloatType)
# type("a") == type(1.0)
# 
# 2.5
# 判断是否是列表
# isinstance("a", ListType)
# type("a") == type([])
# 
# 2.6
# 判断是否是元组
# isinstance("a", Tuple
