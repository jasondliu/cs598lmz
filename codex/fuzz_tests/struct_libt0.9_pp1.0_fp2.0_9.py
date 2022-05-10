import _struct
from model import *
import random
import copy
from utils import *

def read_images(input_file, output_file):
    with open(input_file, 'rb') as f:
        magic, num, rows, cols = _struct.unpack('>4I', f.read(16))
        images = _struct.unpack('>' + 'B' * num * rows * cols, f.read(num * rows * cols))
        images = [images[i : i + rows * cols] for i in range(0, len(images), rows * cols)]
    
    with open(output_file, 'wb') as f:
        f.write(_struct.pack('>4I', magic, num, rows, cols))
        for i in range(num):
            f.write(_struct.pack('>' + 'B' * rows * cols, *(images[i])))
    return images

def read_labels(input_file, output_file):
    with open(input_file, 'rb') as f:

