import mmap

from PIL import Image, ImageFilter
import pyximport
pyximport.install()
from img_fast import *

from settings import *


def find_text(in_img_path, out_img_path, min_width=10, min_height=10,
              filter_alpha=0.8, filter_delta=0):
    in_img = Image.open(in_img_path)
    print 'image open', in_img
    width, height = in_img.size
    out_img_dir, out_img_name = os.path.split(out_img_path)
    out_img_name, out_img_ext = os.path.splitext(out_img_name)
    out_img_ext = out_img_ext.lower()
    out_img_name = '%s_%d_%d_%d_%d_%d_%d' % (out_img_name, width, height,
                                             min_width, min_height,
                                             filter_alpha * 100,

