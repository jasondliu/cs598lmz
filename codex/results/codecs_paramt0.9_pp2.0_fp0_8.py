import codecs
codecs.register_error('punctuation', 'ignore')

#This is a helper function that takes a word and adds it to the dictionary if its not already in there
#It also frees the word of punctuation and sets it to lower case.

def free_word(word):
    word = word.strip().lower()
    word = word.replace('.', '')
    word = word.replace('"', '')
    word = word.replace(',', '')
    word = word.replace('(', '')
    word = word.replace(')', '')
    word = word.replace('`', '')
    word = word.replace(':', '')
    word = word.replace('-', '')
    return word

def add_word(word, hash, sample):
    if word in hash:
        hash[word] = hash[word] + 1
    else:
        hash[word] = 1
#This is the main function that takes the file and sends it to free_word and add_word
def create_hash(file_path, hash, samp):
    word_count
