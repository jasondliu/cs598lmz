import bz2
bz2.BZ2Decompressor.decompress
import gzip
import dill
dill.dumps
import base64
import hashlib
hashlib.md5
import binascii
binascii.hexlify
import json
json.loads
import urllib
urllib.request
import urllib2
urllib2.Request
import xmlrpclib
xmlrpclib.ServerProxy
import uuid
uuid.uuid4

import collections
from collections import *
from collections import OrderedDict, Counter
from collections import deque

from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso, Ridge, ElasticNet

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
