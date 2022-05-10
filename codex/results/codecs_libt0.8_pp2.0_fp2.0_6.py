import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

from KaggleWord2VecUtility import KaggleWord2VecUtility
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation

stops=set(stopwords.words("english"))
print "load data..."

clean_train_reviews=[]

for review in train["review"]:
    clean_train_reviews.append(KaggleWord2VecUtility.review_to_wordlist(review,True))

trainDataVecs = getAvgFeatureVecs( clean_train_reviews, model, num_features )

print "Creating average feature vecs for test reviews"

clean_test_reviews = []
for review in test["review"]:
    clean_test_reviews.append( KaggleWord2VecUtility.review_to_wordlist( review, \
        remove
