import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import svm
from sklearn.decomposition import NMF, TruncatedSVD
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
def clean_review(raw_review):
	review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
	letters_only = re.sub('[^a-zA-Z]', ' ', review_text)
	words = letters_only.lower().split()
	stops = set(stopwords.words("english"))
	meaningful_words = [w for w in words if not w in stops]
	return(" ".join(meaningful_words))
data = p
