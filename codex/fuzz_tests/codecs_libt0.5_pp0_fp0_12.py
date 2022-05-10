import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 %s <file_name>" % sys.argv[0])
        sys.exit(0)
    file_name = sys.argv[1]

    # read file
    with open(file_name, 'r') as f:
        content = f.read()
    f.close()

    # split content into sentences
    sentences = sent_tokenize(content)

    # split sentences into words
    words = [word_tokenize(sent) for sent in sentences]

    # tag words
    pos_words = [nltk.pos_tag(word) for word in words]

    # chunk words
    chunked_sentences = nltk.ne_chunk_sents(pos_words, binary=True)

    # extract named entity
    named_entities = []
    for tree in chunked_sentences:
        named_ent
