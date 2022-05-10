import select_features
from select_features import *
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn.base import clone

from keras.models import Sequential
from keras import layers
from sklearn.model_selection import KFold, train_test_split

from catboost import Pool, CatBoostRegressor
from catboost import cv
import catboost

from sklearn.feature_selection import SelectKBest  ## feature selection: chi-squared
from scipy.stats import chi2_contingency
from functools import partial

from sklearn.ensemble import ExtraTreesRegressor, AdaBoostRegressor, BaggingRegressor, RandomForestRegressor ## , BaggingRegressor, ExtraTreesRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree.tree import DecisionTreeRegressor
from sklearn.feature_selection import SelectFromModel
