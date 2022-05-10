import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_file_encoding(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read()
    try:
        encoding = chardet.detect(rawdata)['encoding']
        if encoding is None:
            encoding = 'utf-8'
    except:
        encoding = 'utf-8'
    return encoding

def _get_file_content(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read()
    try:
        encoding = chardet.detect(rawdata)['encoding']
        if encoding is None:
            encoding = 'utf-8'
    except:
        encoding = 'utf-8'
    content = rawdata.decode(encoding, 'strict')
    return content

def _get_file_content_with_encoding(filename, encoding):
    with open(filename, 'rb') as f:
        rawdata = f.read()
    content = rawdata.dec
