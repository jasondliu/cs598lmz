import codecs
codecs.register_error('replace_spaces', codecs.replace_errors('?', ' '))
#word_re = re.compile(ur'\b[\w-]+\b', re.UNICODE)
word_re = re.compile(ur'\b[\w-]+\b', re.UNICODE)

# TODO: make a method that takes a list of tweets, lemmatizes all the words,
# and repackages them all into an updated list of tweets

def split_words(data):
    words = []
    for tweet in data:
        for word in word_re.findall(tweet.text):
            word = word.strip(punct)
            if word.startswith("#"):
                words.append("#" + word[1:])
            elif word.startswith("@"):
                words.append("@" + word[1:])
            else:
                words.append(word)
    return words

def tweets_to_words(data):
    """
        Extracts words from tweets, converts to lower
