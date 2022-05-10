import gc, weakref

from random import choice
from math import ceil

from os.path import join, split, exists
from os import makedirs

from matplotlib import pyplot as plt
from matplotlib.backends import backend_agg

from pytagcloud import create_tag_image, make_tags, LAYOUT_MIX
from pytagcloud.colors import COLOR_SCHEMES, random_color_func

from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ImageOps import equalize

from nltk.corpus import stopwords
from nltk import tokenize

from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError

from wordcloud_cli.utils import logging, pil_to_array, get_int_from_hex, \
                                get_hex_from_int, get_exif_orientation, \
                                get_arabic_support
from wordcloud_cli.masker import Masker

logger = logging.getLogger
