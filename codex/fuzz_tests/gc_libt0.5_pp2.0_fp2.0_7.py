import gc, weakref
import os, sys

import numpy as np

import numpy.random as npr

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import theano
import theano.tensor as T

import lasagne

from lib import networks as net
from lib import layers as lyr
from lib import updates as upd
from lib import inits as init
from lib import objectives as obj
from lib import metrics as met
from lib import training as train
from lib import utils as utl

from lib.utils import floatX, intX

from lib.plotting import plot_images
from lib.plotting import plot_images_grid
from lib.plotting import plot_lines

from lib.data_utils import shuffle
from lib.data_utils import iter_data
from lib.data_utils import create_batches
from lib.data_utils import create_minibatches

from lib.param_utils import count_params
from lib.param_utils import set_model_params
from lib.param_utils import get_model_params

