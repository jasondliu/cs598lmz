from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)
#
#
# origs = pickle.load(open('E:/data/dbpedia/definitions.pkl', 'rb'))
# origs = {k[2:-2] : v['en'][0] for k,v in origs.items() if 'en' in v}
#
# pickle.dump(origs, open('E:/data/dbpedia/abstracts.pkl', 'wb'))

# origs = pickle.load(open('E:/data/dbpedia/abstracts.pkl', 'rb'))
# tmp = {k : tokenize(v)[:40] for k,v in origs.items()}
# pickle.dump(tmp, open('E:/data/dbpedia/tokenized.pkl', 'wb'))

# pickle.dump(word2vec.wv.vocab, open('E:/wikidump/en/en-vocab.pkl', 'wb'))

# word2vec.wv.save
