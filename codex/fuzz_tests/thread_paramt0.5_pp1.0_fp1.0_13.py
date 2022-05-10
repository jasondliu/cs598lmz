import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import cv2, math, time
import numpy as np
from PIL import Image
import pytesseract
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as colors
from matplotlib.patches import Rectangle

from ocr_functions import *
from ocr_main import *
from ocr_params import *

from tqdm import tqdm
from sklearn.preprocessing import normalize
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as score

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn import preprocessing

from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression

