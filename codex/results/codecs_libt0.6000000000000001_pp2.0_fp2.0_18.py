import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 重新加载sys模块，设置默认字符串编码方式为utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 定义转换函数
def conv(data):
    if isinstance(data, unicode):
        return data.encode('utf-8')
    elif isinstance(data, str):
        return data
    elif isinstance(data, collections.Mapping):
        return dict(map(conv, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(conv, data))
    else:
        return data

# 将字典中的unicode转换为utf8
def unic
