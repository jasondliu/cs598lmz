import weakref
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.distributions import Categorical
from torch.distributions.normal import Normal
#logging with python logger
logging.basicConfig(format='[%(levelname)s] %(message)s',level=logging.INFO)

def save_checkpoint(state, filename):
    torch.save(state, filename)

def load_checkpoint(filename):
    return torch.load(filename)

class Actor(nn.Module):
    def __init__(self, num_inputs, num_outputs, act_func, scale, use_wscale):
        super(Actor, self).__init__()
        self.actor = nn.Sequential(
            nn.Linear(num_inputs, 128),
            nn.BatchNorm1d(128),
            act_func,
            nn.Linear(128,128),
            nn.BatchNorm1d
