import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('replace_with_space'), replace_with_space)

def clean_text(text):
    text = text.replace('<br />', ' ')
    text = text.replace('--', ' ')
    text = text.replace('\'', ' ')
    text = text.replace('[', ' ')
    text = text.replace(']', ' ')
    text = text.replace('.', ' ')
    text = text.replace(',', ' ')
    text = text.replace('?', ' ')
    text = text.replace('!', ' ')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.replace('"', ' ')
    text = text.replace('*', ' ')
    text = text.replace(';', ' ')
    text = text.replace(':', ' ')
    text = text.replace('\n', ' ')
    text = text.replace('\
