import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import pytesseract
from PIL import Image
import re
import pandas as pd
import datetime
import time
import requests
import json
import sys
import csv
import io
import urllib
import urllib.request
import urllib.parse
import urllib.error
import base64
import json
import sys
import os
import requests
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from datetime import datetime
import time
import pytesseract
from pytesseract import Output
from pytesseract import image_to_string
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
from PIL import ImageOps
