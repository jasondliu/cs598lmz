import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_encoding(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read(100)
    return chardet.detect(rawdata)['encoding']

def get_encoding_alternative(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read(100)
    return chardet.detect(rawdata)['encoding']

def convert_to_utf8(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read()
    encoding = get_encoding(filename)
    if encoding is not None:
        try:
            data = rawdata.decode(encoding=encoding)
        except UnicodeDecodeError:
            encoding = get_encoding_alternative(filename)
            data = rawdata.decode(encoding=encoding)
        data = data.encode('utf-8')
        with open(filename, 'wb') as f:
            f
