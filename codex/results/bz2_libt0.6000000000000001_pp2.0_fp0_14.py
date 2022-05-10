import bz2
bz2_data = bz2.BZ2File('data/train.ft.txt.bz2')
data = [x.decode('utf-8') for x in bz2_data.readlines()]
print(data[0])

import re
from nltk.corpus import stopwords

def clean_str(string):
    """
    Tokenization/string cleaning for dataset
    Every dataset is lower cased except
    """
    string = re.sub(r"\\", "", string)
    string = re.sub(r"\'", "", string)
    string = re.sub(r"\"", "", string)
    string = re.sub(r"\n", "", string)
    string = re.sub(r"\r", "", string)
    string = re.sub(r"\t", "", string)
    string = re.sub(r"\xa0", "", string)
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)

