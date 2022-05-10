import sys, threading
threading.Thread(target=lambda: sys.__stdin__.read(1)).start()

def set_trace():
    from IPython.core.debugger import Pdb
    Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)

def jupyter_notebook():
    from IPython import get_ipython
    return get_ipython() is not None and get_ipython().__class__.__name__ == 'ZMQInteractiveShell'

if jupyter_notebook():
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm


import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, sampler
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

from allennlp.modules.elmo import Elmo, batch_to_ids
from allennlp.data.tokenizers.word_tokenizer
