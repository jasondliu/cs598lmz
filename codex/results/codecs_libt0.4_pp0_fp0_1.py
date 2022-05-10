import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np
import datetime
import os
import re
from collections import defaultdict
from functools import reduce
from itertools import combinations
from scipy.stats import chi2_contingency, fisher_exact
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, roc
