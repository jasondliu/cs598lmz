import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Read a file and split into lines
def read_file(filename):
    return codecs.open(filename, "r", encoding="utf-8").read().strip().split('\n')

import nltk
nltk.download('punkt')

# Split a document into news sentences
def to_lines(doc):
    return doc.strip().split('\n')

# Evaluate the skill of the model
def evaluate_model(model, tokenizer, source, raw_dataset):
    actual, predicted = list(), list()
    for i, raw_text in enumerate(raw_dataset):
        # translate encoded source text
        raw_text = raw_text.replace("&amp;", "&")
        raw_text = raw_text.replace("&gt;", ">")
        raw_text = raw_text.replace("&lt;", "<")
        raw_text = raw_text.replace("&quot;", '
