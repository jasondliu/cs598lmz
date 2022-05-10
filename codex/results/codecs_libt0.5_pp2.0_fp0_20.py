import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Data preprocessing
#import re
#from nltk.corpus import stopwords
#from nltk.stem.porter import PorterStemmer
#from nltk.stem import WordNetLemmatizer

#from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
#from sklearn.cross_validation import train_test_split
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.metrics import confusion_matrix, accuracy_score


# In[3]:

def preprocess(dataset):
    data = dataset['text']
    corpus = []
    for i in range(0, len(data)):
        review = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.
