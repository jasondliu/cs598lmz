import codecs
codecs.register_error('replace_spaces', lambda e: (u'?', e.start + 1))

def read_file(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='replace_spaces') as f:
        return f.read()

def write_file(filename, content):
    with codecs.open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def get_words(text):
    return re.findall(r'\w+', text.lower())

def get_word_count(words):
    return Counter(words)

def get_words_in_file(filename):
    return get_words(read_file(filename))

def get_word_count_in_file(filename):
    return get_word_count(get_words_in_file(filename))

def get_word_count_in_files(filenames):
    return reduce(lambda x, y: x + y, map(get_word_count_in_file, filenames
