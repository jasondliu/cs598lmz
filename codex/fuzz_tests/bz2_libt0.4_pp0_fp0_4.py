import bz2
bz2_file = bz2.BZ2File('dataset.json.bz2')

data = []
for line in bz2_file:
    data.append(json.loads(line))

# Check the number of reviews
print(len(data))

# Check one review
pprint(data[1])

# Check the keys of the first review
print(data[0].keys())

# Check the first review text
print(data[0]['reviewText'])

# Check the first review summary
print(data[0]['summary'])
