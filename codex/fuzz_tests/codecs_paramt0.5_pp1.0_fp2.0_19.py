import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def get_words(doc):
    """
    Given a document, return a list of all tokens in the document.
    """
    tokens = []
    for sentence in doc.sentences:
        tokens += [t.text for t in sentence.tokens]
    return tokens

def get_lemma_counts(doc):
    """
    Given a document, return a dictionary mapping lemmas to the number of times
    they appear in the document.
    """
    lemmas = {}
    for sentence in doc.sentences:
        for token in sentence.tokens:
            lemma = token.lemma
            if lemma not in lemmas:
                lemmas[lemma] = 0
            lemmas[lemma] += 1
    return lemmas


def get_pos_counts(doc):
    """
    Given a document, return a dictionary mapping POS tags to the number of times
    they appear in the document.
    """
    pos = {}
    for sentence
