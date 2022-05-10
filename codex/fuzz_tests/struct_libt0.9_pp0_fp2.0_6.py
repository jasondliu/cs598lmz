import _struct
import tensorflow as tf

# DL4J base methods
from deeplearning4j.nn.conf.layers.variational import VariationalAutoencoder

# Numpy / Scipy
import numpy as np
import scipy.io.wavfile as wav

# Visualizations
from IPython.display import Audio
import matplotlib.pyplot as plt
from matplotlib import gridspec
import seaborn as sns

# DL and IO
import time
import os
from collections import namedtuple
import hashlib
import tarfile

# DL4J
from deeplearning4j.iterators.sequencerecordreaderdatasetiterator import SequenceRecordReaderDataSetIterator
import org.datavec.api.records.reader.SequenceRecordReader
import org.datavec.api.records.reader.impl.csv.CSVSequenceRecordReader
import org.datavec.api.split.NumberedFileInputSplit

# DL4J model
from deeplearning4j.core.conf import WorkspaceConfiguration
from deeplearning4j.core.conf
