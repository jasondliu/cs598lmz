import mmap
import numpy as np
from PIL import Image
from tqdm import tqdm
from tensorflow.keras import Sequential, Model
from tensorflow.keras.layers import Reshape, Input, Dense, Conv2D, Flatten, MaxPooling2D, Dropout, BatchNormalization, LeakyReLU
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Activation, Add
from tensorflow.keras.callbacks import ReduceLROnPlateau, ModelCheckpoint, EarlyStopping
from tensorflow.python.keras.losses import mean_absolute_error
from tensorflow.python.keras.metrics import mean_absolute_error as mean_absolute_error_metric
from tensorflow.keras.utils import Sequence
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.utils import shuffle
from sklearn.utils.multiclass import unique_labels
from sklearn.utils.class
