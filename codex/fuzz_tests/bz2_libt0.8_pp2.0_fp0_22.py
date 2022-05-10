import bz2
bz2.__version__

!mkdir ~/.kaggle

!cp kaggle.json ~/.kaggle/

!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d rmisra/news-headlines-dataset-for-sarcasm-detection #downloads the dataset

!unzip /content/news-headlines-dataset-for-sarcasm-detection.zip #unzips the dataset


# Training
import json
import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

vocab_size = 10000
embedding_dim = 16
max_length = 120
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000

with open("/content/Sarcasm_Headlines_Dataset.json", 'r') as f:
    datastore = json.load(f)

