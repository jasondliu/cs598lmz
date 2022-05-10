from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b).decode('utf-8')

#计算在内容中至少出现三次的单词及出现的次数
import re
pat = re.compile(r'\w+')
text1 = '"Ethics are built right into the ideals and objectives of the United Nations" #UNSG @ NY Society for Ethical Culture bit.ly/2guVelr'
pat.findall(text1)

#计算词频
import re
from collections import Counter
count = Counter(pat.findall(text1))
count.most_common(10)

#查找词干
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
[porter.stem(w) for w in pat.findall(text1)]
