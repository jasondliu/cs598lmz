import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import re
import os
import math
import copy
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.io.wavfile as wavfile


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def spectrogram_feature(spec, fs, vad_window, feature_window, window_length, hop_length, n_fft):
    # convolve
    convolved_feature = signal.convolve(spec, vad_window, mode='same', method='direct')
    # get feature
    feature = signal.convolve(convolved_feature, feature_window, mode='same', method='direct')
    # resample
    feature_length = math.floor(feature.shape[1] * (window_length/n_fft) / (fs * hop_length/1000))
    #
