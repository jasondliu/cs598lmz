from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# 如果你使用的是更高级的编码格式，比如XML或者JSON，可以使用对应的解析库来解析数据。
# 但是，通常情况下实现这些协议并不难。例如，下面是一个解析简单的XML格式的例子：
from xml.etree.ElementTree import XML, fromstring, tostring
doc = XML('<root><a>Hello</a><b>World</b></root>')
print(doc.findtext('a'))
print(doc.
