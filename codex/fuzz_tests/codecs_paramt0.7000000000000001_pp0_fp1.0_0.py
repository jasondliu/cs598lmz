import codecs
codecs.register_error('strict', codecs.ignore_errors)
import re
from multiprocessing import Pool
from functools import partial
from pathlib import Path
from collections import defaultdict
from bs4 import BeautifulSoup
from tqdm import tqdm
from tld import get_tld
from langdetect import detect
import logging
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.metrics import
