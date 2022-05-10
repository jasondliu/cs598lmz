import types
types.ModuleType = ModuleType

from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession

from pyspark.sql import HiveContext

from pyspark.sql import SQLContext
from pyspark.sql import functions as F
from pyspark.sql.functions import udf
from pyspark.sql.functions import lit

from pyspark.sql import types as T
from pyspark.sql.types import TimestampType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import DoubleType
from pyspark.sql.types import ArrayType
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField

import pandas as pd
import numpy as np
import re
import time
import datetime

import os
import sys

from functools import reduce

# from IPython.core.display import display, HTML
# display(HTML("<style>.container { width:100% !important; }</style>"))


