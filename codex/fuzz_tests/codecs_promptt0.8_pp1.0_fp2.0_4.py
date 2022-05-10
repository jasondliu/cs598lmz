import codecs
# Test codecs.register_error('My Error', MyError)

from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import json
import random
from datetime import datetime
import time
from collections import defaultdict
import exifread
from gps_coordinate_conversion import gps_to_utm, utm_to_gps
import piexif
from copy import copy
import struct
from fractions import Fraction
import binascii
import pymysql
from pymysql.err import InternalError

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.mllib.linalg import SparseVector
from pyspark.mllib.feature import HashingTF, IDF

from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import CrossValid
