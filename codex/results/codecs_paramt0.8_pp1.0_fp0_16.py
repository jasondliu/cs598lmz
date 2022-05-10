import codecs
codecs.register_error('sub',sub)

# 打印错误信息
def print_error():
    try:
        print(u'a'.encode(encoding='ascii',errors='sub'))
    except UnicodeEncodeError as e:
        print(e)
print_error()
