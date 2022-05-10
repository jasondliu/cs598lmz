import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_def_with_id(id):
    """
    Given the id of the definition, returns the definition
    """
    definition = db.session.query(Definition).get(id)
    return definition

def get_word_with_id(id):
    """
    Given the id of the word, returns the word object
    """
    word = db.session.query(Word).get(id)
    return word

def get_similar_words(word):
    """
    Given the word, returns a list of similar words
    """
    similar_words = db.session.query(Word).filter_by(word=word).all()
    return similar_words

def get_all_words():
    """
    Returns a list of all words
    """
    all_words = db.session.query(Word).all()
    return all_words

def get_all_definitions():
    """
    Returns a list of all definitions
