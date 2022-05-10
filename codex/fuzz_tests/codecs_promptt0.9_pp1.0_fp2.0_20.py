import codecs
# Test codecs.register_error


def decode(instr):
    return instr.encode('unicode-escape').decode('ascii')


def encode(ustr):
    return ustr.encode('ascii').decode('unicode-escape').encode('utf-16le')


for error in ['replace', 'ignore', 'backslashreplace', 'xmlcharrefreplace',
              'namereplace', decode, encode]:

    text = 'ab\xe1'
    utf7 = b'ab&AGEC-.'
    utf8 = b'ab\xc3\xa1'
    utf16 = b'ab\xa1\x00'
    latin1 = b'ab\xa1'
    cp437 = b'ab\x81'
    uu = b"begin 666 <data>\nM0D5'24X97)O86P\n \nend\n"
    base64 = b"YWJhAAD//w=="

    data = [(utf8, "utf-8", error), (utf7, "utf-7", error
