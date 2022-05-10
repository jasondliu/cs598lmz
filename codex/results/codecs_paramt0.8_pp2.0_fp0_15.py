import codecs
codecs.register_error('replace_with_space', 
                     lambda e: (u' ', e.start + 1))   

def clean_text(text):
    text = text.replace('@', '')
    text = text.replace('#', '')
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace(';', '')
    text = text.replace('&amp;', 'and')
    text = text.replace('...', ' ')
    text = text.replace('RT ', ' ')
    text = text.replace('"', '')
    text = ' '.join(word for word in text.split() if word[0] != '@' and word[0] != '#')
    return text

class TwitterSentimentAnalysis:
    def __init__(self, classifier=RandomForestClassifier()):
        self.classifier = classifier
        self.vectorizer = TfidfVectorizer(
            tokenizer=self.tokenize_and_stem,
            preprocessor=self.preprocessor
