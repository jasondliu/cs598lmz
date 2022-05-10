import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import sys
import os
import time
from datetime import datetime, timedelta
from dateutil import parser
import json
import re
import string
from pprint import pprint
from bson import ObjectId
from pymongo import MongoClient
import pymongo
from pymongo import UpdateOne
from pymongo import InsertOne
from pymongo import DeleteMany
from pymongo import ReplaceOne
from pymongo import BulkWrite
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix

