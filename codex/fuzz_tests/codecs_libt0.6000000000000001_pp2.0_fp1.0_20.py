import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Open the file with read only permit
f = open('../data/raw/raw_data_train.txt')
# use readline() to read the first line
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    # print(line)
    print(line.strip())
    # use realine() to read next line
    line = f.readline()
f.close()

# Open the file with read only permit
f = open('../data/raw/raw_data_test.txt')
# use readline() to read the first line
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is
