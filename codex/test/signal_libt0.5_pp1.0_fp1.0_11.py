import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QFileDialog
from PyQt5.QtCore import Qt

from src.src.utils.file_utils import read_file, save_file
from src.src.utils.data_utils import get_vocab, get_vocab_size
from src.src.utils.tokenizer import tokenize
from src.src.utils.embedding_utils import load_embedding_matrix
from src.src.utils.data_utils import get_index_from_sentence

from src.src.utils.model_utils import make_model
from src.src.utils.model_utils import load_model
from src.src.utils.model_utils import predict

from src.src.utils.plot_utils import plot_attention_weights
