import threading
threading.stack_size(2**27)
import sys
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
import numpy as np
import random
import os
import csv
import time
import sys
import matplotlib.pyplot as plt

# -------------------- BRAIN ---------------------------
class Brain():
    def __init__(self, stateCnt, actionCnt):
        self.stateCnt = stateCnt
        self.actionCnt = actionCnt

        self.model = self._createModel()
        self.model_ = self._createModel()  # target network

    def _createModel(self):
        model = models.Sequential()
        model.add(layers.Dense(units=64, activation='relu', input_dim=stateCnt))
        model.add(layers.Dense(units=32, activation='relu'))
        model.add(layers.Dense(units=actionCnt, activation='linear'))
