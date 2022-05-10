import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, column, lit, when, concat, split, udf, isnan, isnull, from_unixtime, unix_timestamp, to_timestamp, date_format, regexp_replace, lower, upper, trim, array, explode, create_map, struct, collect_list, collect_set, size, coalesce, count, sum, max, min, avg, mean, stddev, variance, skewness, kurtosis, corr, countDistinct, approx_count_distinct, first, last, ntile, percent_rank, cume_distinct, row_number, dense_rank, rank, lag, lead, nth, lag, lead, nth, cume_distinct, row_number, dense_rank, rank, lag, lead, nth, dense_rank, percent_rank, cume_distinct, row_number, dense_rank, rank, lag, lead, nth, dense_rank, percent_
