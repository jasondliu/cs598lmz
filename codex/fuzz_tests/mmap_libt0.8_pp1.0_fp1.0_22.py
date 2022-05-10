import mmap
from src.variables import *
from src.load_data import *
from src.utils import *
from src.tk_canvas import Paint,Setting
from src.tensorflow_model import *
from src.keras_model import *
from src.sklearn_model import *
import pandas as pd
from PIL import Image
from io import BytesIO
from base64 import b64encode
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from scipy import stats
from sklearn.cluster import KMeans

#from sklearn.neural_network import MLPClassifier
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.svm import SVC
#from sklearn.gaussian_process import GaussianProcessClassifier
#from sklearn.gaussian_process.kernels import RBF
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
#from sklearn.naive_bayes import Ga
