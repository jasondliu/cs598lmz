import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_content(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_content_as_list(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

def get_file_content_as_list_of_words(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read().split()

def get_file_content_as_list_of_words_and_punctuation(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return re.findall(r"[\w']+|[.,!?;]", f.read())

def get_file_content_as_list_of_words_and_punctuation_and_new
