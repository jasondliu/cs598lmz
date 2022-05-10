import threading
threading.stack_size(2 ** 27)
import sys
import time
from datetime import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS

from lib.utils.load_config import load_config
from lib.utils.data_loader import load_data
from lib.utils.tokenizer import load_tokenizer
from lib.utils.model_loader import init_model
from lib.utils.utils import set_seed

from lib.generate.generate_utils import *

app = Flask(__name__)
CORS(app)

# Load configuration
config = load_config()

# Load data
data = load_data(config)

# Load tokenizer
tokenizer = load_tokenizer(config)

# Load model
model = init_model(config, tokenizer)

# Set seed
set_seed(config.seed)

# Load encoder
encoder = Encoder(config, data, tokenizer)

# Load generator
generator = Generator(config, data, tokenizer)

# Load decoder

