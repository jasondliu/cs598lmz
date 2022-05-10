from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 可以使用format字符串来创建一个结构体，
# 字符串中的每个字符都表示一个C类型，
# 可以使用标准的struct模块字符串或者使用Python的原生字符串
# 如果使用原生字符串，那么在字符串中的每个字符之前都要加上一个问号
# 如果使用标准的struct模块字符串，那么就不需要
