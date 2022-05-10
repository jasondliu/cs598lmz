import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_text(file_name):
    with codecs.open(file_name, encoding='utf-8', errors='strict') as f:
        return f.read()

def get_words(text):
    return re.findall(r'\w+', text.lower())

def get_words_from_file(file_name):
    return get_words(get_text(file_name))

def get_words_from_files(file_names):
    return [w for file_name in file_names for w in get_words_from_file(file_name)]

def get_words_from_dir(dir_name):
    return get_words_from_files(glob.glob(dir_name + '/*'))

def get_words_from_dirs(dir_names):
    return [w for dir_name in dir_names for w in get_words_from_dir(dir_name)]

def get_words_from_text(text):
    return get
