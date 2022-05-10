import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

def test(encoding):
    print '-'*50
    print 'Encoding:', encoding
    print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a')
    print 'decode:', repr('\x82\xa0\x82\xa2\x82\xa4\x82\xa6\x82\xa8')
    print '-'*50
    print

for encoding in ['iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004',
                  'iso2022_jp_3', 'iso2022_jp_ext', 'shift_jis', 'euc_jp',
                  'euc_jis_2004', 'euc_jisx0213', 'shift_jisx0213',
                  'shift_
