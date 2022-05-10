import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def clean_text(text):
    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')
    text = text.replace('\t', ' ')
    text = re.sub(r'[ ]+', ' ', text)
    text = re.sub(r'[\s]+', ' ', text)
    text = text.strip()
    return text

def clean_text_for_scoring(text):
    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')
    text = text.replace('\t', ' ')
    text = re.sub(r'[ ]+', ' ', text)
    text = re.sub(r'[\s]+', ' ', text)
    text = text.strip()
    return text

def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in stopwords.
