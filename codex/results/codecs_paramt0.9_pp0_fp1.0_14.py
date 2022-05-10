import codecs
codecs.register_error('replace_ascii', codecs.replace_errors)
from scipy.sparse import *
from scipy import *
from sklearn.svm import *
from sklearn.neighbors import *
from sklearn import tree
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LogisticRegression as LogR
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold

# FIXME: посмотреть, обобщается ли ансамбль при разных параметрах разделения на кластеры

def create_clustering(X, labels, n = 10):
    from sklearn.cluster import KMeans

    kmeans = KMeans(n_cl
