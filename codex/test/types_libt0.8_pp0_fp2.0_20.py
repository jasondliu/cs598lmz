import types
types.ModuleType('sklearn.cross_validation').__dict__.update(
    __import__('sklearn.model_selection', fromlist=['cross_validation']
               ).__dict__)

from sklearn.cross_validation import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


# def load_data(filename: str):
#     data = np.loadtxt(filename, delimiter=',', dtype=float)
#     return [data[:, :-1], data[:, -1]]


def process_data(filename: str, test_size=0.2):
    data = np.loadtxt(filename, delimiter=',', dtype=float)
    X
