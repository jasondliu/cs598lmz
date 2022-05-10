import threading
threading.stack_size(2**27)

from flask import Flask
import time
import scipy.io as sio
import json
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import pickle
from collect import Google_Play_Callable, App_Store_Callable

import signal, sys,os
from base64 import b64decode
# set the headers for the server
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

