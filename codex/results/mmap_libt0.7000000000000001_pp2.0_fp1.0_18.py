import mmap
import random
import time
import subprocess
import math
import collections
import threading
import sys
import copy
import socket

import multiprocessing
#from multiprocessing import Process

# This needs to be here or we get an import error
from evaluation.eval_utils import *

import numpy as np

from pyspark import SparkContext, SparkConf, StorageLevel
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *

from evaluation.eval_utils import *
from utils import *
from job_utils import *

conf = (SparkConf()
        .setMaster("local[*]")
        .setAppName("My app")
        .set("spark.executor.memory", "4g"))
sc = SparkContext(conf = conf)
sqlCtx = SQLContext(sc)

# If you change this, you MUST change the "class" param below
num_updates = 10

# The keys in this dict are what will be passed to the executor job
# The values are lists of the arguments that
