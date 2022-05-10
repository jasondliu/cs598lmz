import codecs
codecs.register_error('surrogate_or_nonprintable_replace', codecs.replace_errors)

def detect_encoding(filename):
    try:
        with open(filename, 'rb') as fh:
            rawdata = fh.read(32)
    except Exception as e:
        return 'unknown'
    else:
        if not rawdata:
            return 'unknown'
    encodings = ['utf-8', 'windows-1250', 'windows-1252', 'ascii']
    for enc in encodings:
        try:
            rawdata.decode(enc)
        except UnicodeDecodeError:
            pass
        except Exception as e:
            return 'unknown'
        else:
            return enc

def get_data(filename, kind, encoding='utf-8', **kwargs):
    if kind == 'spacy':
        for line in codecs.open(filename, 'r', encoding, errors='surrogate_or_nonprintable_replace'):
            line = line.strip()
            if not line:
                continue
            yield line
