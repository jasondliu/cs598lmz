import codecs
# Test codecs.register_error

# Test multi-byte codecs
def test_main():
    for encoding in ['iso2022_jp', 'hz', 'iso8859_1', 'utf_8', 'utf_16_be',
                     'utf_16_le', 'utf_16', 'utf_32_be', 'utf_32_le',
                     'utf_32']:
        if encoding.startswith('iso2022_jp'):
            start = 0x21
        else:
            start = 0x41
        for i in range(start, start + 26):
            c = chr(i) * 10
            try:
                e = c.encode(encoding)
            except:
                pass
            else:
                e = e[:-1] + b'\x80'
                try:
                    codecs.decode(e, encoding)
                except UnicodeDecodeError:
                    pass
                else:
                    print('%s: Error not raised' % encoding)

    # Test single-byte codecs
    for encoding in ['base64_codec', 'base32
