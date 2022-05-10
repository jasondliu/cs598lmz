import codecs
codecs.register_error('replace_with_space', replace_with_space)

def handle_punctuation(text):
    return text.translate(None, string.punctuation)

def handle_digits(text):
    return re.sub('\d+', ' ', text)

def preprocess(sentence):
    sentence = sentence.strip()
    sentence = sentence.lower()
    sentence = handle_punctuation(sentence)
    sentence = handle_digits(sentence)
    sentence = sentence.split()
    sentence = [word for word in sentence if word not in stopwords.words('english')]
    sentence = ' '.join(sentence)
    return sentence

def build_corpus(data_file):
    """Creates a list of lists containing words from each sentence
    * data_file *string* filename containing preprocessed data
    """
    corpus = []
    with open(data_file, encoding='utf-8') as data:
        for line in data:
            corpus.append(line.split())
    return corpus

def get_frequency_
