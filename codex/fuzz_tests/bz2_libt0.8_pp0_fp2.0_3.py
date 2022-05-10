import bz2
bz2_file = 'sample.bz2'

with bz2.BZ2File(bz2_file) as file:
    content = file.read()
    print(content)

with open(bz2_file[:-4], "wb") as outfile:
    outfile.write(content)

    # https://stackoverflow.com/questions/32856866/how-to-append-lines-to-a-bz2-file-in-python


import bz2
import os
#bz2_file = 'sample.bz2'
bz2_file = 'sample.json.bz2'

with bz2.BZ2File(bz2_file, 'rb') as f:
    for i in range(10):
        print(f.readline().decode('utf-8'))
        
import json
import os
with open('test.json') as file:
    parsedJSON = json.load(file)
    print(len(parsedJSON))
    print(parsedJSON[
