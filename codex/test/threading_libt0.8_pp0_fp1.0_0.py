import threading
threading.stack_size(2**20)

from utils.segmenters.segmenter import Segmenter
from utils.muse_utils import load_embedding_weight, tokenize

from utils.model_utils import get_model, get_optimizer


# In[4]:


def get_module(module_name):
    return importlib.import_module('.' + module_name, __name__)


# In[5]:


def main():
    parser = argparse.ArgumentParser(description="Chinese word segmentation")
    parser.add_argument("--gpu", action="store_true", help="Using GPU")
    parser.add_argument("--mode", type=str, help="train, eval or predict")
    parser.add_argument("--model", type=str, help="The type of model")
    parser.add_argument("--segmenter", type=str, help="The type of segmenter, determine input & output format")
