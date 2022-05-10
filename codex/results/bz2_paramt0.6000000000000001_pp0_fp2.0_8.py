from bz2 import BZ2Decompressor
BZ2Decompressor()

# This is the format of each line:
# "ip_address,unix_timestamp,status_code,total_bytes"
# There are no headers, and the fields are separated by commas

# Create a SparkContext with Spark configuration
sc = SparkContext(appName="Exercise 38")

# The directory to the data files
inputPath = "/data/spark7/access_log_aug95"

# Create an RDD from the log file using a textFile method
# Each element of an RDD is a line from a file
augLogsRDD = sc.textFile(inputPath)

# Split each line into a list of items
# The map transformation applies a function to each element of the RDD
# In this case, the function is the Python built-in split function,
# which splits each line into a list of items
itemsRDD = augLogsRDD.map(lambda line: line.split(","))

# The map transformation returns a new RDD
print type(itemsRDD)

# The new RDD is composed of lists, where each list is a line
