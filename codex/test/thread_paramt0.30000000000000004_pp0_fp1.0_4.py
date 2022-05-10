import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

#Create a DataFrame from a list of values
df = spark.createDataFrame([(1,2,3,'a b c'),
                            (4,5,6,'d e f'),
                            (7,8,9,'g h i')],['A','B','C','D'])
df.show(truncate=False)

#Split the column value into multiple rows
df.withColumn('D',f.split('D',' '))\
  .select('A','B','C',f.explode('D').alias('D'))\
  .show(truncate=False)

#Split the column value into multiple rows with a column for position
