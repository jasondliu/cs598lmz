import mmap, os
from collections import Counter, defaultdict, deque
from scipy import stats
import pandas as pd
from Hyperparameters import Embedding_Size, Window_Size, Quantize_Level, Data_Set, debug_size, start, sparse_size, num_lstm_unit, Min_Count
from Embedding import EmbeddingModel
from DataSet import DataSet
from Scoring import Scoring
from Tuner import Tuner
from Evaluator import Evaluator
from utils import display_text
from utils import Timer, printer
from tree import BinaryTree
from loop import Loop_Scoring

result_list = []
title_list = ['Iteration', 'Validation', 'Deprel', 'Pos', 'Train', 'Test', 'Test2', 'Validation_W_A', 'Validation_W_B', 'Validation_W_label', 'Validation_W_label_(Counter)', 'Validation_W_label_(most)', 'Validation_W_label_(t)', 'Validation_W_label_(dev)', 'Validation_W_
