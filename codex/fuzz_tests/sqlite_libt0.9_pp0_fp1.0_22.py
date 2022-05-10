import ctypes
import ctypes.util
import threading
import sqlite3
import time
from datetime import datetime
import json
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
import math
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
from datetime import datetime
from collections import Counter



# ==================================================
#       Declarations
# ==================================================

lock = threading.Lock()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "0.0.0.0"
server_port = 8888

