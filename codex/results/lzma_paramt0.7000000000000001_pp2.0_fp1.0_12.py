from lzma import LZMADecompressor
LZMADecompressor().decompress(open('stack_overflow_data.7z', 'rb').read()).decode('utf-8')

# load the data again
df = pd.read_csv('stack_overflow_data.csv')

df.head()

# find the shape of the DataFrame
df.shape

# word count in each of the answers
df['word_count'] = df['answer'].apply(lambda x: len(str(x).split(" ")))
df[['answer', 'word_count']].head()

# find the average word length of each answer
def avg_word(sentence):
  words = sentence.split()
  return (sum(len(word) for word in words)/len(words))

df['avg_word'] = df['answer'].apply(lambda x: avg_word(x))
df[['answer', 'avg_word']].head()

# find the number of stopwords in each answer
from nltk.corpus import stopwords
stop = stopwords.words('english')

df['stopwords
