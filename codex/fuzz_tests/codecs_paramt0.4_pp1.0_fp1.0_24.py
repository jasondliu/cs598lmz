import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The pre-trained model
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=500000)

# The words we want to find similarities for
words = ['dog', 'cat', 'mouse', 'computer', 'laptop', 'tablet', 'smartphone', 'phone', 'table', 'chair', 'couch', 'bed', 'pillow', 'blanket', 'shower', 'bathtub', 'sink', 'toilet', 'door', 'window', 'wall', 'floor', 'ceiling', 'roof', 'tree', 'bush', 'flower', 'grass', 'rock', 'sand', 'water', 'ocean', 'lake', 'river', 'stream', 'pool', 'pond', 'cliff', 'mountain', 'hill', 'valley', 'desert', 'beach', 'cave', 'canyon', 'dune', 'forest', 'jungle', 'meadow', 'park', 'plains', 'plate
