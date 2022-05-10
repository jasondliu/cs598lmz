import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_similarity(phrase1, phrase2, skipgram_path, word_dimension):
    word_similarity_map = {}
    for i in phrase1:
        for j in phrase2:
            if i not in word_similarity_map:
                word_similarity_map[i] = {}
            if j not in word_similarity_map[i]:
                word_similarity_map[i][j] = get_skipgram_similarity(i, j, skipgram_path, word_dimension)
    return word_similarity_map

def get_skipgram_similarity(word1, word2, skipgram_path, word_dimension):
    word1_vector = [0] * word_dimension
    with codecs.open(skipgram_path, 'r', 'utf-8') as r:
        for line in r:
            l = line.split()
            if len(l) <= 1:
                continue
           
