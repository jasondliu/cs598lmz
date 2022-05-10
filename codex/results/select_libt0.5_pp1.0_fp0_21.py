import select
import sys
import time

import numpy as np
import pandas as pd
import psutil
import requests
from sklearn import preprocessing

from data_collector import DataCollector
from data_preprocessor import DataPreprocessor
from model_evaluator import ModelEvaluator
from model_trainer import ModelTrainer
from model_visualizer import ModelVisualizer
from utils import Utils
from utils import log


class Main:
    def __init__(self):
        self.config = None
        self.data_collector = None
        self.data_preprocessor = None
        self.model_trainer = None
        self.model_evaluator = None
        self.model_visualizer = None
        self.utils = None
        self.model = None
        self.scaler = None
        self.df = None
        self.df_test = None
        self.df_train = None
        self.df_val = None
        self.df_pred = None
        self.pred_data = None
        self.pred_target =
