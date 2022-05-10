import mmap
import re
import sys
import datetime

# * output.txt > output_engine.txt
# * output.txt is compatible with output01.txt, output02.txt, ...
# * engine and host information are added to each line of output01.txt, output02.txt, ...

parameters = ["DATE_TIME","USER","HOST","SERVER_ID","CONNECTION_ID","SERVER","START_TIME","END_TIME","TRANSACTION_COUNT","TOTAL_DURATION","MAX_DURATION","MIN_DURATION","ERROR_COUNT","RECONNECT_COUNT","ERROR_LOG","ENGINE","TOTAL_FETCH_COUNT","TOTAL_FETCH_BYTES","LOCAL_FETCH_COUNT","LOCAL_FETCH_BYTES","LOCAL_FETCH_AVG_BYTES","LOCAL_FETCH_AVG_DURATION","REMOTE_FETCH_COUNT","REMOTE_FETCH_AVG_DURATION","INT_BYTES","INT_PACK
