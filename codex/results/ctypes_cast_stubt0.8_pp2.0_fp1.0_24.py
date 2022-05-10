import ctypes
ctypes.cast(std_out.stream, ctypes.py_object).value = sys.stdout
ctypes.cast(std_err.stream, ctypes.py_object).value = sys.stderr

# @register_line_magic
# def stop_spark_session(line):
#     global spark
#     if spark is not None:
#         spark.sparkContext.stop()
#         spark = None
#         print("Stopped Spark Session")
#         return
#     print("No Spark Session running")


# @register_line_magic
# def start_spark_session(line):
#     global spark
#     if spark is not None:
#         print("Spark Session already running")
#         return
#     spark = SparkSession.builder.getOrCreate()
#     print("Started Spark Session")

# print("To stop Spark Session: %stop_spark_session")
# print("To start Spark Session: %start_spark_session")
# %stop_spark_session
#%start_spark_session
 
 
 

