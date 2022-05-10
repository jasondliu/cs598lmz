import codecs
# Test codecs.register_error

import codecs, _codecs_cn, _codecs_kr, _codecs_jp, _codecs_tw, _codecs_hk

encoding = 'gbk'

def search_function(encoding):
    if encoding == 'test.unicode.gbk':
        return codecs.getregentry('gbk')

codecs.register(search_function)

tstring = ('\xc2\xeb\xcf\xee\xd1\xd4\xd0\xf8\xd5\xc2\xca\xd4\xbf\xc9\xbc\xf6'
           '\xc8\xcb\xc3\xf1\xd3\xeb\xb9\xab\xb0\xd7\xb8\xc4\xd2\xc2\xab\xb1'
           '\xbb\xad\xd3\xd0\xb9\xe6\xc7\xeb\x20\x28\x6e\x6f\x72\x6d\
