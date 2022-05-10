import mmap
import struct
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
from PIL import ImageChops
import cv2
import numpy as np
import os

# For Python 2
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# For Python 3
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# For Python 2
#import urllib2
# For Python 3
import urllib.request

# For Python 2
#import urlparse
# For Python 3
import urllib.parse

# For Python 2
#from cStringIO import StringIO
# For Python 3
from io import BytesIO

# For Python 2
#import json
# For Python 3
import json

# For Python 2
#import Tkinter as tk
# For Python 3
import tkinter as tk

# For Python 2
#from Tkinter import *
# For Python 3

