import codecs
codecs.register_error('replace_with_space',
                      lambda e: (u' ', e.start + 1))

def strip(text):
    return text.translate({ord(c): None for c in string.whitespace})

def read_text(filename):
    with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
        return f.read()

def write_text(filename, text):
    with codecs.open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

def read_text_lines(filename):
    with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

def write_text_lines(filename, lines):
    with codecs.open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def read_json(filename):
    with codecs.open(
