import lzma
lzma.decompress(open("C:/Users/Maulik/Downloads/wiki-en-test.txt.xz","r").read())

#df = pd.read_csv("C:/Users/Maulik/Downloads/wiki-en-test.txt", usecols=["article"])
df1 = pd.read_csv("C:/Users/Maulik/Downloads/wiki-en-test.txt", usecols=["article"])
df1.head()

#cleaning the articles
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def process_article(article):
    tokens=word_tokenize(article)
    stop=stopwords.words("english")
    output=[i for i in tokens if not i in stop]
    output=re.sub("[^a-zA-Z]"," ",str(output))
    output=output.lower()
    return output

#nltk.download("punkt")
#nltk.download("stopwords
