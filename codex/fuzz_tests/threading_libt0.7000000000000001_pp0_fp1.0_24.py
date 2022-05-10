import threading
threading.stack_size(67108864)  # 64MB stack

import numpy as np
import tensorflow as tf

from audio import Vocabulary, load_vocab, load_audio, spectrogram_to_mel, augment_audio
from model import CNNTranslator, CNNTranslator_v2, CNNTranslator_v3
from plot import plot_spectrogram, plot_alignment

from tqdm import tqdm
from sklearn.model_selection import train_test_split

from hparams import hparams
import time

from utils import *


def main(args):
    # Load vocabulary
    # target_vocab = Vocabulary(load_vocab(args.dataset_path, "targets.txt"),
    #                           pad='<pad>', eos='<eos>', bos='<bos>', unk='<unk>')
    # source_vocab = Vocabulary(load_vocab(args.dataset_path, "sources.txt"),
    #                           pad='<pad>', eos='<eos>
