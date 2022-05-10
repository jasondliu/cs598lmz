import threading
threading.stack_size(2**28)
import numpy as np

from sim_utils import *
from base_net import Net
from pong_sim import Pong_Sim


class Pong_Net(Net):
    def __init__(self, name, state_shape, num_actions, trainer, model_num=1,
                 num_convs=2, conv_filter_sizes=[8, 4], conv_filter_nums=[16, 32],
                 num_fc_layers=2, fc_layer_sizes=[256,], discount=0.99,
                 entropy_beta=0.05, max_grad_norm=0.5,
                 policy_lr=1e-4, value_lr=1e-3,
                 rollout_length=5, rollout_batch_size=1,
                 rollout_threads=1):
        super(Pong_Net, self).__init__(name, state_shape, num_actions, trainer, model_num,
                 num_convs, conv_filter_sizes, conv_filter_nums,

