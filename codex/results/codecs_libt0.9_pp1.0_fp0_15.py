import codecs
codecs.register(register_aliases)
from comet_ml import Experiment, ExistingExperiment

from utils.util_func import str2bool
from models import make_model
from data_loaders import make_data_loader
from utils.util_func import calculate_acc, calculate_mean_auc, make_prediction
from utils import nn_utils

# Training setting
parser = argparse.ArgumentParser(description='DeepHP')
parser.add_argument('--model_name', type=str, default='na', help='name of model')
parser.add_argument('--config', type=str, default='everynetwork_lstm')
parser.add_argument('--dataset', type=str, default='ssb', help='dataset name: Cotrain/SSB/Feng/RR/Yeast/Plants/PPI')
parser.add_argument('--seq_len', type=int, default=250)
parser.add_argument('--train_set', type=str, default='train', help='the set used for training')
parser.add_argument
