from bz2 import BZ2Decompressor
BZ2Decompressor()

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

import pickle

from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english'))


path = "/content/drive/My Drive/FINAL YEAR/collection.json.bz2"
f = bz2.open(path, "r")


sum = 0
x = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in f:
	sum = sum + 1
	if(sum < 1112249 and sum > 1112239):
		x[sum - 1112240] = line
	elif(sum > 1112249):
		break



data1
