import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class Classifier(BaseEstimator):
    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english', ngram_range=(1,2), min_df=2)
        self.lsi = TruncatedSVD(n_components=500, random_state=42)
        self.k_means = KMeans(n_clusters=1000, random_state=42)
        self.scaler = StandardScaler()
        self.clf = RidgeClassifier(tol=1e-2, solver="lsqr", random_state=42)
        self.clf1 = RandomForestClassifier(n_estimators=500, random_state=42)
        self.clf2 = MultinomialNB()
        self.clf3 = LogisticRegression(C=1, random_
