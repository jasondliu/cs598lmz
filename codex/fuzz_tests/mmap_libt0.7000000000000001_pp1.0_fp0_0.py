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
    lines = map(lambda x: x.split('|')[0], lines)
    return lines

def get_wavfile_paths(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    lines = content.split('\n')
    lines = filter(lambda x: len(x) > 0, lines)
    return lines

def filter_files(files, min_duration=0, max_duration=None):
    min_duration = min_duration * hparams.sample_rate
    max_
