import ctypes
ctypes.cast(0, ctypes.py_object).value = None
import sys
sys.path.append('/home/nrupatunga/research/sml/code/python/')
from sml.utils import *
from sml.sml import *
from sml.ml.ml import *
from sml.ml.classification.random_forest import RandomForest
from sml.ml.classification.svm import SVM
from sml.ml.classification.logistic_regression import LogisticRegression


def main():

    # Get the training and testing data
    dataset = '/home/nrupatunga/research/sml/data/msrc_obj_detect/'
    (train_images, train_labels, train_masks,
     test_images, test_labels, test_masks) = get_data(dataset)

    # Create the classifiers and set the parameters
    svm_classifier = SVM()
    log_reg_classifier = LogisticRegression()
    random_forest = RandomForest()

    # Set the parameters
