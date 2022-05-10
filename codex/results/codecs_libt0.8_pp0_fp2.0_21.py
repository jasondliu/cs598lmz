import codecs
codecs.BOM_UTF16

# sys.path.append('..')
# print(sys.path)

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

#from src.train import load_data
from train import load_data
import numpy as np

#from scipy.sparse import lil_matrix
from scipy.sparse import hstack

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neural_network import MLPClassifier


def main():
    # Load the training data
    X, y = load_data('data/
