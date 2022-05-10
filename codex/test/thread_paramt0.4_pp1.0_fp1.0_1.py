import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from collections import defaultdict

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import window
from pyspark.sql.types import StructType

spark = SparkSession.builder.appName("StructuredNetworkWordCount").getOrCreate()

userSchema = StructType().add("ID","string").add("Lang","string").add("Date","string").add("Source","string").add("len","integer").add("Likes","integer").add("RTs","integer").add("Hashtags","string").add("UserMentionNames","string").add("UserMentionID","string").add("Name","string").add("Place","string").add("Followers","integer").add("Friends","integer")

csvDF = spark.readStream.option("sep", ";").schema(userSchema).csv("/stream")

