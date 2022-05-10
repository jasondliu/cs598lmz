from bz2 import BZ2Decompressor
BZ2Decompressor()

# This is the format of each line:
# "ip_address,unix_timestamp,status_code,total_bytes"
# There are no headers, and the fields are separated by commas

# Create a SparkContext with Spark configuration
