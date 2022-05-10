import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', errors='replace_with_space') as f:
        return f.read()

def write_file(filename, text):
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(text)

def get_text(filename):
    text = read_file(filename)
    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('\v', ' ')
    text = text.replace('\f', ' ')
    text = text.replace('\b', ' ')
    text = text.replace('\a', ' ')
    text = text.replace('\0', ' ')
    text = text.replace('\1', ' ')
    text = text.replace('\2
