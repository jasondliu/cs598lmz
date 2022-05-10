import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_encoding(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        header = f.readline()
        if not header.startswith('#'):
            return 'utf-8'
        for line in header.splitlines():
            if line.startswith('# -*- coding:'):
                _, encoding = line.split(':')
                encoding = encoding.strip()
                return encoding
    return 'utf-8'

def load_po(filename):
    encoding = get_encoding(filename)
    with open(filename, 'r', encoding=encoding) as f:
        return polib.pofile(f, encoding=encoding)

def save_po(filename, po):
    encoding = get_encoding(filename)
    with open(filename, 'w', encoding=encoding) as f:
        po.save(f, encoding=encoding)

def get_members(mo, po):
    members = set()
    for
