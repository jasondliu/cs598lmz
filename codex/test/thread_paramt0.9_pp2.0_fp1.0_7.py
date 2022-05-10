import sys, threading
threading.Thread(target=lambda: sys.stdin.read()).start()
import sys
sys.path.append("../")
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_curve, auc
from sklearn.cross_validation import train_test_split
import numpy as np
from keras.models import model_from_json
from keras.callbacks import Callback
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras import backend as K
from MLP import MLP
from utils import get_tissue_from_image_name
from DataGenerator import DataGenerator
from clr import cyclic_learning_rate

class Adam_lr(Callback):
    def __init__(self, base_lr, max_lr, step_size, ref_acc=0.95):
        self.base_lr = base_lr
        self.max_lr = max_lr
        self.base_momentum = 0.9
        self.max_momentum = 0.999
        self
