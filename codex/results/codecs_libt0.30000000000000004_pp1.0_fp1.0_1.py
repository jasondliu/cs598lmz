import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# read the file
with open('C:/Users/mohamed ismail/Desktop/python/data.csv', 'r') as f:
    data = f.readlines()

# remove the first row (contains headers)
data = data[1:]

# split the rows by comma and append them to a new list
data_no_comma = []
for row in data:
    splitted_row = row.split(',')
    data_no_comma.append(splitted_row)

# remove the \n from the last element in each row
data_no_new_line = []
for row in data_no_comma:
    fixed_row = row[:-1] + [row[-1].replace('\n', '')]
    data_no_new_line.append(fixed_row)

# remove the double quotes from each element in the dataset
data_no_quotes = []
for row in data_no_new
