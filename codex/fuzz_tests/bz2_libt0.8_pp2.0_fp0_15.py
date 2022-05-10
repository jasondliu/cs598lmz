import bz2
bz2.decompress(f.read()).decode('utf-8')

# To get the values we need to look inside the text and extract the
# information. It looks like the data is in json format and we can use 
# python's json library to parse the data.

import json
data = json.loads(bz2.decompress(f.read()).decode('utf-8'))

# It's useful to look at what the data looks like as well.

data[0]

#
# TASK 1
#
# print out the number of reviews of the first restaurant
#
print(f"The first restaurant has {data[0]['review_count']} reviews")

#
# TASK 2
#
# print out the first review
#
print(data[0]['reviews'][0])

#
# TASK 3
#
# print out "business_id", "name" and "categories" for the first business in the dataset
# Hint: Use a for loop to access all of the values in the dict.
#
