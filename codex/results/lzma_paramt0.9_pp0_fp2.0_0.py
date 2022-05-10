from lzma import LZMADecompressor
LZMADecompressor()
d = pickle.load(gzip.open('../../data/pickkle/fifa_top_n.pkl.gz', 'rb'))
df = pd.DataFrame(d)
df.tail()

#with open('data/pickkle/fifa_top_n_2017_11.pkl', 'rb') as f:
#    d = pickle.load(f)

#df = pd.read_pickle('data/pickkle/fifa_top_n_2017_11.pkl')
