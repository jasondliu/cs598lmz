import mmap
import sys
from datetime import datetime
from collections import defaultdict

# use the name of the file to extract the name of the model
# e.g. log_15-06-16_18-37-45.log -> 15-06-16_18-37-45
def get_model_name(filename):
    return filename.split('_')[1].split('.')[0]

# parse the log file
# extract the model name and the total number of parameters from the first line
# extract the epoch and the validation loss from the last line
def parse_log(filename):
    with open(filename, 'r') as f:
        # extract the model name from the first line
        model_name = get_model_name(filename)
        # extract the number of parameters from the first line
        line = f.readline()
        params = int(line.split()[-1])
        # jump to the last line
        f.seek(0, os.SEEK_END)
        while f.tell() > 0:
            line = f.readline()
