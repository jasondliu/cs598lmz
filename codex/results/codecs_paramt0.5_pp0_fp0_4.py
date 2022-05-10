import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Read in the data
with codecs.open('../data/text/spanish_sentences.txt', 'r', 'utf-8', errors='replace_with_space') as f:
    data = f.read()

# Replace punctuation with tokens so we can use them in our model
data = data.lower()
data = data.replace('.', ' <PERIOD> ')
data = data.replace(',', ' <COMMA> ')
data = data.replace('"', ' <QUOTATION_MARK> ')
data = data.replace(';', ' <SEMICOLON> ')
data = data.replace('!', ' <EXCLAMATION_MARK> ')
data = data.replace('?', ' <QUESTION_MARK> ')
data = data.replace('(', ' <LEFT_PAREN> ')
data = data.replace(')', ' <RIGHT_PAREN> ')
data = data.replace('--', ' <HYPH
