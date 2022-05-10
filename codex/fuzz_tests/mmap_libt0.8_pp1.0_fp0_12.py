import mmap
import webcolors
import os
import sys
import shutil
from io import BytesIO
from PIL import Image
from jubatus.recommender import client as jubareco
from jubatus.recommender import types as jubatypes
from jubatus.common import Datum

config = {
    'host': '127.0.0.1',
    'port': 9199,
    'name': '',
    'timeout': 10,
}
if len(sys.argv) == 4:
    config['host'] = sys.argv[1]
    config['port'] = int(sys.argv[2])
    config['name'] = sys.argv[3]

# #############################################################################
# make dataset
def load_image(image_path):
    image = Image.open(image_path)
    image.load()
    return image.resize((256,256)).convert('RGB')

def dominant_color(image):
    image = image.convert('RGBA')
    image.thumbnail((200, 200
