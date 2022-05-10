import bz2
bz2.BZ2File(data_file).read()

data_file = "data/train.json.bz2"
data = bz2.BZ2File(data_file).read()

data_file = "data/train.json.bz2"
data = bz2.open(data_file).read()

data_file = "data/train.json.bz2"
data = bz2.open(data_file, 'r')
data.read()
data.close()

data_file = "data/train.json.bz2"
data = bz2.open(data_file, 'r')

for line in data:
    print(line)
    
data.close()

data = bz2.open(data_file, 'r')

for line in data:
    print(line[:-1])
    
data.close()

data = bz2.open(data_file, 'r')

for line in data:
    print(line[:-1].decode('utf-8'
