from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("data/testing_data.bz2", "rb").read())

# Read in the training data.
train_data = []
with open("data/training_data.json") as f:
    for line in f:
        train_data.append(json.loads(line))
# Read in the test data.
test_data = []
with open("data/testing_data.json") as f:
    for line in f:
        test_data.append(json.loads(line))

#print(train_data[0], '\n', test_data[0])
# The training data is a list of dictionary objects. Each dictionary has the
# form:
#   {
#       "stars": number of stars (1 through 5)
#       "text": text of the review,
#       "type": "review" or "business"
#       "business_id": id of the business
#   }
#
# The test data follows the same format.

# You can access a list's elements using list[index].
# For example:
#
