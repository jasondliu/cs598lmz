import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('ignore'))

def clean_text(text):
    '''
    Clean text by removing unnecessary characters and altering the format of words.
    '''
    text = text.lower()
    text = text.replace(r"i'm", "i am")
    text = text.replace(r"he's", "he is")
    text = text.replace(r"she's", "she is")
    text = text.replace(r"it's", "it is")
    text = text.replace(r"that's", "that is")
    text = text.replace(r"what's", "that is")
    text = text.replace(r"where's", "where is")
    text = text.replace(r"how's", "how is")
    text = text.replace(r"\'ll", " will")
    text = text.replace(r"\'ve", " have")
    text = text.replace(r"\'re", " are")
    text = text.replace(r"\'d", "
