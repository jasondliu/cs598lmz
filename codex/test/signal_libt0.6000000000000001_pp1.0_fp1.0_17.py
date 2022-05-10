import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

from utils import *
from data import *
from models import *
from losses import *
from metrics import *
from trainer import *

def main():
    parser = argparse.ArgumentParser(description='PyTorch Training')
    parser.add_argument('--exp_name', type=str, default='default', help='experiment name')
    parser.add_argument('--dataset', type=str, default='svhn', help='dataset name')
    parser.add_argument('--out_dir', type=str, default='outputs', help='output directory name')
    parser.add_argument('--gpu', type=int, default=0, help='GPU id to use.')
    parser.add_argument('--n_epochs', type=int, default=200, help='number of epochs')
    parser.add_argument('--batch_size', type=int, default=100, help='batch size')
