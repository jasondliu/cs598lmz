import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

text = open('sample.txt', encoding='UTF-8').read()
len(text)

text = text.lower()
text = text.replace('\n', ' ')

# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
len(tokens)


# remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
len(words)

# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
len(words)
print(words)

postags = nltk.pos_tag(words)
print(postags)
