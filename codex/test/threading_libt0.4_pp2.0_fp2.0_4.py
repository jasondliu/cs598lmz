import threading
threading.Thread(target=lambda: None).start()

import time
time.sleep(3)

import sys
sys.path.append('/home/ubuntu/workspace/utils')

import numpy as np
import pandas as pd
import datetime as dt
import os
from pathlib import Path
import pickle
import requests
import json
import csv
import urllib.request
import urllib.parse
import urllib.error
import base64
import http.client, urllib.request, urllib.parse, urllib.error, base64

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
