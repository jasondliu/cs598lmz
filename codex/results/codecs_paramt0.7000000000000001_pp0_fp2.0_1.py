import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def text_cleaner(text):
    text = text.lower()
    text = re.sub('[\n\r\t]',' ', text)
    text = re.sub(u'[\u200B-\u200D\uFEFF]',' ', text)
    text = re.sub('[^\w\s]',' ', text)
    text = re.sub('_', ' ', text)
    text = re.sub('[\s+]', ' ', text)
    text = text.strip()
    return text


def get_text_from_file(path):
    try:
        with codecs.open(path,'r', errors='replace_with_space') as file:
            return text_cleaner(file.read())
    except:
        return ''


def text_from_files(files):
    return [get_text_from_file(path) for path in files]


def filter_files(files):
    return [file for file
