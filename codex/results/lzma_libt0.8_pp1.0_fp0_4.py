import lzma
lzma.open
from pathlib import Path
from shutil import copyfile

from fastai.script import *
from fastai.vision import *
from fastai.distributed import *
from fastai.callbacks import *

from sklearn.metrics import precision_score, recall_score, fbeta_score
import pandas as pd
from IPython.display import FileLink
 
from torchvision.models import vgg16_bn

#basepath = Path('/kaggle/grapheme/')
#data_path = basepath/'data'

# URL: https://www.kaggle.com/iafoss/grapheme-fastai-starter-kfold-cv-lb-0-971
# by: Iafoss

# read data and make training set
PATH = Path('./grapheme_fastai')

def read_training_data(in_path):
    train = pd.read_csv(in_path/'train.csv')
    train_labels = pd.read_csv(in_
