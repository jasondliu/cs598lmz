import lzma
lzma.compress('test')

# バイナリデータをそのまま文字列として扱う
# encodeメソッドでは文字列からbytes型に変換
# decodeメソッドではbytesから文字列に変換
# str.encode('オプション')
# bytes.decode('オプション')

s = 'あいうえお'
s.encode('utf-8') # b'\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a'
s.encode('cp932') # b'\x82\xa0\x82\xa2\x82\xa4\x82\xa6\x82\xa8'

b = b'\x82\xa0\x82\xa2\x82\xa4\
