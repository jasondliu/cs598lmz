import codecs
# Test codecs.register_error.
# In GBK, the sequence b'\xa2\xae' means nothing
class MyError(Exception):
    pass

def illegal_gbk(exc):
    if isinstance(exc, UnicodeDecodeError):
        ch = exc.object[exc.start:exc.end]
        return (ch, exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('gbk_error', illegal_gbk)

#text = 'Hello world! \xa2'
#print(codecs.decode(text, 'gbk'))
data = pd.read_csv('C:\\Users\\admin\\Desktop\\yh.csv',encoding='gbk')
print(data.head())
# print(data['处理状态'])
# print(data['处理状态'].str.contains('已联系'))
