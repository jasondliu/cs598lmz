from lzma import LZMADecompressor
LZMADecompressor()

import time
start = time.time()
# Create a JSON file, in which the output will be stored.
fp = open('hong_kong_sar_china.json', 'w')

# Type of the file, which we are going to read.
filename = 'hong_kong_sar_china.csv'

# We need this in order to be able to identify the type of each cell.
type_dict = defaultdict(str)

# Max number of rows that are going to be read into memory.
num_rows_in_memory = 500 * 1000

# Initialize dicts containing the infos from the csv rows.
current_dict = defaultdict(list)
previous_dict = defaultdict(list)

with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
    countries_file = csv.reader(f)
    header_1 = next(countries_file)
    header_2 = next(countries_file)
    header_3 = next(countries_file)
    header_
