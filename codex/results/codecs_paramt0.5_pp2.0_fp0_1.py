import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def get_tokens(file_name):
    with open(file_name, 'r', encoding='utf-8', errors='replace_with_space') as file:
        tokens = file.read().split()
    return tokens

def get_tokens_from_url(url):
    return get_tokens(get_file_from_url(url))

def get_file_from_url(url):
    file_name = url.split('/')[-1]
    if not os.path.isfile(file_name):
        with open(file_name, 'wb') as file:
            file.write(requests.get(url).content)
    return file_name

def get_words_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8', errors='replace_with_space') as file:
        words = file.read().split()
    return words

def get_words_from_url(url
