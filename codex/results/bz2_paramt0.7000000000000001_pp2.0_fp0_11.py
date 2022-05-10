from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(line).split()

# In[23]:

# 分词
import jieba
seg_list = jieba.cut(text)
' '.join(seg_list)

# In[24]:

# 抽取词干
from nltk.stem.snowball import SnowballStemmer
snowball_stemmer = SnowballStemmer('english')
snowball_stemmer.stem('responsiveness')

# In[25]:

# 词性标注
import nltk
text = "I am Jack's raging bile duct."
nltk.pos_tag(nltk.word_tokenize(text))

# In[26]:

# 拼写校验
import re
from collections import Counter
def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS
