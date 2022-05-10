import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from a thread\n')).start()

from IPython.display import display, HTML
display(HTML('<h1>Hello from IPython.display</h1>'))

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("Test").getOrCreate()

df = spark.read.json("python/test_support/sql/people.json")
df.show()
