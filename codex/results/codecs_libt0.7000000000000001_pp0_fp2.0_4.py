import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

from my_modules import *
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

'''
this script is to predict the action of a sentence
'''

# general
sentences = read_csv('c:\\Users\\tomer\\Documents\\Sentences_dataset\\dataset.csv')
sentences = sentences.drop(columns=['Unnamed: 0'])
sentences = sentences.dropna()
sentences = sentences.sample(frac=1).reset_index(drop=True)

# get data of the target language
sentences = sentences[sentences['lang'] == 'en']

# divide the dataset to 2 groups - one with the subject and one without
sentences_with_subj = sentences[sentences['subj'] != '[]']
sentences_with_subj =
