import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
# codecs.register_error('strict', codecs.replace_errors)
# print(codecs.lookup_error('strict'))
# print(codecs.lookup_error('ignore'))
# print(codecs.lookup_error('replace'))
# print(codecs.lookup_error('backslashreplace'))
# print(codecs.lookup_error('xmlcharrefreplace'))
# print(codecs.lookup_error('namereplace'))

# 使用编解码器接口
# result = codecs.encode('abc', 'rot_13')
# print(result)
# print(codecs.decode(result, 'rot_13'))

# 对于不支持解码的编码器，返回错误
# result = codecs.encode('abc
