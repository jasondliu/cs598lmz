import mmap
import numpy as np
import os
from scipy.io import wavfile
from scipy.signal import resample
from tqdm import tqdm

from hparams import hparams
from utils import audio

def get_training_files(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    lines = content.split('\n')
    lines = filter(lambda x: len(x) > 0, lines)
