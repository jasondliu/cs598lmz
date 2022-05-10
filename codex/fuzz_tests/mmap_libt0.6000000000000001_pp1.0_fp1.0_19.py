import mmap
import struct
import json

from masbin.conll import read_conll, write_conll
from masbin.eval import evaluate_conll
from masbin.seg import load_segmenter
from masbin.text import load_text, TokenTokenizer

from flask import Flask, request, jsonify

app = Flask(__name__)

def load_model(model_file):
    with open(model_file, 'r') as f:
        model = json.load(f)

    return model

def load_embeddings(embeddings_file):
    # Load embeddings
    if embeddings_file.endswith('.bin'):
        embeddings = load_embeddings_bin(embeddings_file)
    elif embeddings_file.endswith('.vec'):
        embeddings = load_embeddings_vec(embeddings_file)
    else:
        raise ValueError('Invalid embeddings file type: ' + embeddings_file)

    return embeddings

def load
