import threading
threading.stack_size(64 * 1024 * 1024)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']= '2'
import warnings
warnings.filterwarnings('ignore')
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.utils import *
from src.model import create_model

def to_categorical(y, n_classes):
    y_cat = np.zeros((y.shape[0], n_classes))
    y_cat[range(y.shape[0]), y] = 1
    return y_cat

# def train_stacked_generator(files, model, batch_size, X_test, y_test, directory,
#                             lr=0.001, epochs=100, save_model=True, verbose=2, tresholds=None):
#     """
#     function for training stacked generalization model
#     :param files: list of files to train on
#     :param
