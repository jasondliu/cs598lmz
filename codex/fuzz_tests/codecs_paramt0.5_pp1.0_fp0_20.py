import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_data():
    data = []
    for filename in glob.glob('data/*.txt'):
        with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
            data.append(f.read())
    return data

def extract_features(data):
    vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english', decode_error='replace')
    vectorized = vectorizer.fit_transform(data)
    return vectorized.toarray(), vectorizer

def cluster_data(data, vectorizer):
    km = KMeans(n_clusters=3)
    km.fit(data)
    print "Top terms per cluster:"
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(3):
        print "Cluster %d
