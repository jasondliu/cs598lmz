import codecs
codecs.encode('안녕하세요', 'utf-8')

print(codecs.encode('안녕하세요', 'utf8', 'backslashreplace'))
print(codecs.encode('안녕하세요', 'utf8', 'ignore'))
print(codecs.encode('안녕하세요', 'utf8', 'replace'))

codecs.decode(b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94', 'utf-8')

print(codecs.decode(b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94', 'utf-8',
