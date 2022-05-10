import gc, weakref

import torch
from torch._six import container_abcs, string_classes, int_classes, FileNotFoundError
import numpy as np

from torch.nn.utils.rnn import pad_sequence

from torch_geometric.data import InMemoryDataset
from torch_geometric.data import extract_zip
from torch_geometric.read import read_txt_array
from torch_geometric.read import read_txt_graph
from torch_geometric.read import read_obj
from torch_geometric.read import read_off
from torch_geometric.read import read_ply
from torch_geometric.io import read_txt_array, read_off, read_txt_graph
from torch_geometric.io import read_obj, read_ply


def collate(data_list):
    keys = data_list[0].keys
    return Batch.from_data_list(data_list, keys=keys)


class Batch(object):
    def __init__(self, batch=None, **kwargs):
        assert batch is None or isinstance(
