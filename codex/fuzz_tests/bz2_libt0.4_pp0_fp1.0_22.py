import bz2
bz2.BZ2File('./data/train.ft.txt.bz2')

# Import the data
train_file = bz2.BZ2File('./data/train.ft.txt.bz2')
test_file = bz2.BZ2File('./data/test.ft.txt.bz2')

# Print out the first 4 lines
train_file.readline()
train_file.readline()
train_file.readline()
train_file.readline()

# Print out the first 4 lines
test_file.readline()
test_file.readline()
test_file.readline()
test_file.readline()

# Initialize an empty list: reviews
reviews = []

# Iterate over the lines
for line in train_file:
    
    # Decode the line
    line = line.decode('utf-8')
    
    # Split the line into fields
    fields = line.split('\t')
    
    # Extract the fields
    reviews.append(fields[2
