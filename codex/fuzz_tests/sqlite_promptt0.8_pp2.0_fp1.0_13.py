import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect without the threading.Lock() call
conn = sqlite3.connect('examples.db')
print conn
# convert labeled point from RDD to DataFrame
from pyspark.ml.linalg import Vectors
from pyspark.sql import Row

row_data = [
      Row(label=2.0, features=Vectors.dense(0.0, 0.0, 18.0, 1.0)),
      Row(label=1.0, features=Vectors.sparse(4, [0, 3], [0.0, 3.0]))]
row_df = spark.createDataFrame(row_data)
row_df.show()
# Check spark version
spark.version
# 1.6.2
spark.master
# u'spark://10.0.0.6:7077'

# Check spark local directories
for i in spark.sparkContext._conf.getAll():
    print i

# Check spark.eventLog.enabled
spark.conf.get('spark.eventLog.enabled')
# u
