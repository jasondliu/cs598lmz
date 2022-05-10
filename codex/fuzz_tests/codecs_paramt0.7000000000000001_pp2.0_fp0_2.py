import codecs
codecs.register_error("strict", codecs.ignore_errors)

import librosa
import argparse
import numpy as np
import os
import shutil
import scipy.io.wavfile as wav
import soundfile as sf
import sys
import warnings

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import np_utils
from keras.optimizers import SGD

from sklearn.decomposition import PCA

np.set_printoptions(threshold=np.nan)

def wav2mfcc(file_path):
    # Load the data, resample it to 16000 Hz and apply log-scaling
    y, sr = librosa.load(file_path)
    X = librosa.feature.mfcc(y=y, sr=sr, hop_length=512)
    # Compute first-order delta MFCC features
    delta = librosa.feature.delta(X)
    # Stack and synchronize between mel-spectrogram and delta
    combined
