import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
sys.path.append('../')
from utils.utils import *

#------------------------------------------------------------------------------
# Load data and set training parameters
#------------------------------------------------------------------------------

# Set some parameters
#IMG_WIDTH = 256
#IMG_HEIGHT = 256
#IMG_CHANNELS = 3

#train_path = '../data/train/'
#test_path = '../data/test/'
#train_ids = next(os.walk(train_path))[1]
#test_ids = next(os.walk(test_path))[1]

# Get and resize train images and masks
#X_train = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
#Y_train = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, 1), dtype=
