import codecs
# Test codecs.register_error

import codecs, _codecs_cn, _codecs_kr, _codecs_jp, _codecs_tw, _codecs_hk

encoding = 'gbk'

def search_function(encoding):
    if encoding == 'test.unicode.gbk':
        return codecs.getregentry('gbk')

codecs.register(search_function)

