from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(file_content)
#file_content = file_content.decode('utf-8')

#print(file_content)
#file_content
#data = pd.read_table('data/tweets_corpus.tsv', sep='\t', header=None)
#data.head()

#data[:1000].to_csv('data/tweets_corpus.tsv', sep='\t', header=False, index=False)
#tweets = pd.read_csv('data/tweets_corpus.tsv', sep='\t', header=None)
#tweets.head()

#tweets[1] = tweets[1].str.replace('http\S+|www.\S+', '', case=False)
#tweets[1] = tweets[1].str.replace('@\S+', '', case=False)
#tweets[1] = tweets[1].str.replace('&\S+', '', case=False)
#tweets
