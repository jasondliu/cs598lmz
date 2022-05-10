import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(data['text'][:100]))).start()

# ###################### Download N-grams #########################################

from nltk.util import ngrams
from collections import Counter

# create a placeholder for the data
ngrams = {'unigrams': Counter(), 'bigrams': Counter(), 'trigrams': Counter()}

# this is a bit time consuming - make the if statement True
# if you want to execute data prep yourself.
if 1 == 1:

    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords

    # get the barbara walters dataset
    data = pd.read_csv('https://raw.githubusercontent.com/nicholasmccullum/pydata_pandas/master/data/barbara_walters.csv')

    # extract the text column
    data_text = data[['text']][:1000]

    for index, row in data_text.iterrows():
        tokens = nltk.word_token
