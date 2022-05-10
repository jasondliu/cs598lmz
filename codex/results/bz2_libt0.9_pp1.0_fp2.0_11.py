import bz2
bz2.open()

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import desc, col, asc
import bz2
from os import listdir
from os.path import isfile, join

from pyspark.sql.dataframe import DataFrame
from pyspark.sql.column import Column

def get_page_counts(page_count_file, sqlContext):
    page_count_df = sqlContext.read.format('com.databricks.spark.xml')\
                    .options(rowTag='page', valueTag='count')\
                    .load(page_count_file)
    return page_count_df


# Load page count data from XML files.
def get_all_page_count_df(path, sqlContext):
    page_count_files = [join(path, f) for f in listdir(path) if isfile(join(path, f)) and 'Archive' in
