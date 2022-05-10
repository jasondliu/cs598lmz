import threading
threading.stack_size(2**27)

import spacy
nlp = spacy.load('en')

def preprocess_text(input_text):
    input_text = input_text.strip().replace("\n", " ").replace("\r", " ")
    input_text = REPLACE_BY_SPACE_RE.sub(' ', input_text)
    input_text = BAD_SYMBOLS_RE.sub('', input_text)
    input_text = ' '.join([x for x in input_text.split() if x and x not in STOPWORDS])
    return input_text

def get_lemmas(text):
    doc = nlp(text)
    return [x.lemma_ for x in doc]


def apply_demo(df, text_field):
    df[text_field] = df[text_field].str.lower()
    df[text_field] = df[text_field].apply(preprocess_text)

    # df['city'] = df['city'].fillna('')
   
