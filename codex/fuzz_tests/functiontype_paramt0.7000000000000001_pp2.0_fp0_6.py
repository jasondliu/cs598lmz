from types import FunctionType
list(FunctionType(compile('a > b', '<string>', 'exec'), globals(), 'lambda'))

# ######################################################################################################################
#
# 作用域
#
# 本质上，Python 的作用域一共有 4 种，分别是：
#
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部
