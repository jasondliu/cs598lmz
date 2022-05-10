import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)


def get_tokenized_text(text):
    tokenized_text = nltk.word_tokenize(text)
    return tokenized_text


def get_words_from_tokenized_text(tokenized_text):
    words = [w.lower() for w in tokenized_text if re.search('[a-zA-Z]', w)]
    return words


def get_words_from_text(text):
    tokenized_text = get_tokenized_text(text)
    words = get_words_from_tokenized_text(tokenized_text)
    return words


def get_words_from_file(filename):
    text = get_text_from_file(filename)
    words = get_words_from_text(text)
    return words


def get_text_from_file(filename):
    with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
        text = f.read()
   
