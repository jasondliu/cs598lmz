import threading
threading.stack_size(2**27)

from fp_growth import find_frequent_itemsets
transactions = [('a', 'b', 'c'),
                ('b', 'd'),
                ('a', 'c', 'd', 'e'),
                ('a', 'd', 'e'),
                ('a', 'b', 'c'),
                ('a', 'b', 'c', 'd'),
                ('a'),
                ('a', 'b', 'c'),
                ('a', 'b', 'd'),
                ('b', 'c', 'e')]


from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()
X=vectorizer.fit_transform([' '.join(transaction) for transaction in transactions])


from scipy.spatial.distance import cosine,minkowski
from sklearn.metrics import jaccard_similarity_score,pairwise_distances
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
X=vectorizer
