from bz2 import BZ2Decompressor
BZ2Decompressor.extra_bits = 0

fconfig = '../data/fasttext_configs/setimes_emb300_ngram_chars7_epoch15_wordNgrams4_order.txt'
fword   = '../data/fasttext_models/setimes_emb300_ngram_chars7_epoch15_wordNgrams4'
fembedding = '../data/fasttext_models/setimes_emb300_ngram_chars7_epoch15_wordNgrams4.npy'
ftags = '../data/setimes2-fi/setimes2.fi.train.txt.final'

if not os.path.exists(fconfig):
    input_train = '../data/setimes2-fi/setimes2.fi.train.txt.final'
    input_test  = '../data/setimes2-fi/setimes2.fi.test.txt.final'
    sentences = load_file(input_train) + load_file(input_test)
    word_map, word_tag_map, id
