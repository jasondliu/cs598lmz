from lzma import LZMADecompressor
LZMADecompressor().flush()

import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import json
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_context('talk')
sns.set_style('darkgrid')
sns.set_palette('colorblind')

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

dataset = 'dummy_is'
data_dir = '../data/%s'%dataset
output_dir = '../output/%s'%dataset
ratio = 0.2
compressions = ['lz4','lzma','snappy','zstd']
models = ['gbt','lgb','xgb','cat','par','ker','nn','lst','ffn','3dc','cnn','dnn','bid','rnn','gru','lstm','clstm
