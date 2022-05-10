import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
with open('corpus_cl.txt', encoding = 'utf-8', errors='replace_with_space') as p:
    corpus = p.read().splitlines()
#with open('stopwords_cl.txt', encoding = 'utf-8') as p:
#    stop = p.read().splitlines()

corpus = [w.lower() for w in corpus]

#def tokenise(s):
#    s = re.sub(r'(http[s]?://)?([-\w.])+([:/?%&=]*)?', ' ', s)
#    s = re.sub(r"[<>,\-“”‘’;)(\"]", ' ', s)
#    s = re.sub(r"\.", ' .', s)
#    s = re.sub(r"([0-9])+", ' \g<1>', s)
#    tokens = nltk.word_tokenize(s)
#    return tokens

#corp
