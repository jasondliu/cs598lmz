import types
types.MethodType(sort,tf_idf)

tf_idf.shape

tf_idf.describe()

from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectFromModel
from numpy import sort
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectFromModel

from sklearn.model_selection import *

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn import tree
from sklearn import svm
from sklearn.svm import NuSVR, SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso
