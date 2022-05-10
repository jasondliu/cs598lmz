import bz2
bz2_file = bz2.BZ2File('file.txt.bz2')
print(bz2_file)
import json
json_file = json.load(bz2_file)
print(json_file)
import gzip
gzip_file = gzip.GzipFile('file.txt.gz')
print(gzip_file)

# read the json file
#import json
#import bz2
#import gzip
#
#json_file = open('file.txt')
#json_file.read()
#json_file.close()

def read_json(file_name):
    if file_name.endswith('.json'):
        file = open(file_name)
    elif file_name.endswith('.json.bz2'):
        file = bz2.BZ2File(file_name)
    elif file_name.endswith('.json.gz'):
        file = gzip.GzipFile(file_name)
    else:
        raise ValueError(file_
