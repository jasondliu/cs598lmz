import bz2
# Test BZ2Decompressor

dec = bz2.BZ2Decompressor()
with open("./../data/enwik8.bz2", 'rb') as f:
    with open("./../data/enwik8_dec", 'wb') as f_out:
        for chunk in iter(lambda : f.read(2**20), b''):
            f_out.write(dec.decompress(chunk))
del dec
res = !python -m nltk.downloader -d ./../data/nltk_data stopwords
if res:
    print(res)
del res

import nltk
nltk.data.path.append("./../data/nltk_data")
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

from itertools import chain
from collections import Counter
import random
import string

with open("./../data/enwik8_dec", 'r') as f:
    text = f.read()
del f

chars = list(set(
