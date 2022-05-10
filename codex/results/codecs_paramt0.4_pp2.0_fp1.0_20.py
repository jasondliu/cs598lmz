import codecs
codecs.register_error('strict', codecs.ignore_errors)
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

# nltk.download('wordnet')
# nltk.download('stopwords')

#load the data
df = pd.read_csv("../data/data.csv")

#drop the columns that are not needed
df = df.drop(['Unnamed: 0', 'id', 'url', 'timedelta'], axis=1)

#split the data into training and testing data
train_data, test_data = train_test_split(df, test_size=0.2)
train_data = train_data.reset_index()
test_data = test_data.reset_index()

#function to clean the data
def clean_data(data):
    data['title'] = data['title'].apply(lambda x: x.lower())
    data['title'] = data['title'].apply((lambda x: re.sub('[^a-zA
