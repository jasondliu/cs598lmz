import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

df = pd.read_csv('.ipynb_checkpoints/data.tsv',sep='\t',encoding='utf-8')
df['review'][0]

#2.Data Preprocessing
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', df['review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer
