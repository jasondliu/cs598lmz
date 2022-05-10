import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_files(path):
    files = []
    for root, dirs, file in os.walk(path):
        for f in file:
            files.append(os.path.join(root, f))
    return files

def get_text(file):
    with open(file, 'r') as f:
        text = f.read()
    return text

def get_text_utf8(file):
    with codecs.open(file, 'r', 'utf-8', 'strict') as f:
        text = f.read()
    return text

def get_text_cp1251(file):
    with codecs.open(file, 'r', 'cp1251', 'strict') as f:
        text = f.read()
    return text

def get_text_cp1252(file):
    with codecs.open(file, 'r', 'cp1252', 'strict') as f:
        text = f.read()
    return text

def get_
