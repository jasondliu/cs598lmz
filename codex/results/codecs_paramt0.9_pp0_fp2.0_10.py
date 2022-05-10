import codecs
codecs.register_error('strict', codecs.ignore_errors)
!pip install unpythonic -q
 
!pip install bs4 -q
!pip install lxml -q
!pip install requests -q
!pip install konlpy -q

import requests
from IPython.core.display import display, HTML
from bs4 import BeautifulSoup
from konlpy.tag import Mecab
import csv
import re
import datetime
from datetime import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
from pandas import Series
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import Tfidf
