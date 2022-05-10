import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Create a list of the stopwords
stoplist = stopwords.words('english')

# Load the spacy language model
nlp = spacy.load('en_core_web_sm')

# Create a dictionary of lemmas
lemmas = {}

# Open the lemma file
with open('lemmatization-en.txt') as f:
    # Iterate over all lines
    for line in f:
        # Split the line into key and value
        key, value = line.split()
        # Add to the dictionary
        lemmas[key] = value

# Create a function to lemmatize text
def lemmatize_text(text):
    # Create a list to store the lemmas
    lemmas = []
    # Iterate over the tokens
    for token in nlp(text):
        # Get the lemma for the token
        lemma = token.lemma_
        # If there is no lemma, use the token instead
        if lemma == '
