import io
# Test io.RawIOBase class
test_file = 'path_not_exist'
bf = io.BufferedIOBase(test_file)
os.path.exists(test_file)


# Load a standard dictionary definition of a nltk word tagged with parts of speech 
# and stem
nltk_pos_dictionary = nltk.corpus.cmudict.dict()
assert 'dog' in nltk_pos_dictionary
nltk_pos_dictionary['dog']
nltk_pos_dictionary['runners']
nltk_pos_dictionary['runner']
nltk_pos_dictionary['running']


# Load a standard dictionary definition of a wordnet word tagged with parts of speech 
# and stem
wordnet_pos_dictionary = wordnet.wordnet.synsets('dog')
wordnet_pos_dictionary
wordnet_pos_dictionary = wordnet.wordnet.synsets('runners')
wordnet_pos_dictionary
wordnet_pos_dictionary = wordnet.wordnet.synsets('runner')
wordnet_
