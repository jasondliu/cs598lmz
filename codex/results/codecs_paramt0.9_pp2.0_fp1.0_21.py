import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

def read_file(path, threshold):
    with codecs.open(path, encoding='utf-8', errors='replace') as file:
        text = file.read()
        text = re.sub('<.*>', '', text)
        text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
        try:
            row_tokenize = text.split('\n')
        except UnicodeDecodeError:
            print('No tokenized row for this input')
            row_tokenize = []
        positive_tweets = [x for x in row_tokenize if x.split()]
        print(len(positive_tweets))
        return positive_tweets

path = os.getcwd
