import codecs
codecs.register_error('strict', codecs.ignore_errors)

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

from keras.models import Model
from keras.layers import Input, Dense, Embedding, Concatenate, Dropout, LSTM, GRU, Bidirectional, TimeDistributed, Activation
from keras.layers import Conv1D, MaxPooling1D, GlobalMaxPooling1D, GlobalAveragePooling1D
from keras.preprocessing import text, sequence
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import initializers, regularizers, constraints, optimizers, layers

# set parameters:

max_features = 20000
maxlen = 150
batch_size = 32
embedding_dims = 300
epochs = 10

print('Loading data...')

x_train = np.load('../data/data_train.npy')
y_train = np.load('../data/label_train
