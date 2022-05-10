import mmap
from PIL import Image
import os
from PIL import Image
import datetime
import random
from datetime import datetime
import requests
from io import BytesIO


def get_image_http(url, image_name, image_path):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        img.save(os.path.join(image_path, image_name + '.jpg'))
        return img
    except Exception as err:
        pass
    return None


def is_img(x):
    return x.split('.')[-1] in set(['JPG', 'PNG', 'JPEG'])


def get_img_from_url(url_path, image_path):
    image_names = []
    url_list = []
    with open(url_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if not line.startswith('http'):
            continue
        if line
