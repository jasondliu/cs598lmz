import codecs
codecs.register_error('replace_chars', ErrorHandler)

def get_random_name():
    return random.choice(NAMES)

def _parse_name(file):
    with codecs.open(file, 'r', encoding='utf8', errors='replace_chars') as f:
        unread = f.buffer.raw.read()
    return unread.decode('utf8', 'replace_chars')

#Получает два слова-имени
def get_names():
    name1 = _parse_name(PATH_TO_1)
    name2 = _parse_name(PATH_TO_2)
    return (name1[:-1], name2[:-1])

#Получает строку имени
def get_name():
    return _parse_name(PATH_TO)

def generate_names(n):
    i = 0
    while i < n:
        with open(PATH_TO_3,
