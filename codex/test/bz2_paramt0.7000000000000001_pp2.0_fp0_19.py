from bz2 import BZ2Decompressor
BZ2Decompressor()

# file location
data_file = './data/data.bz2'

# decompress the file
# with open(data_file, 'rb') as raw_file:
#     decompressor = BZ2Decompressor()
#     decompressed_data = decompressor.decompress(raw_file.read())

# write the decompressed file
# with open('./data/data.json', 'wb') as json_file:
#     json_file.write(decompressed_data)

# call the API and get the data
# response = requests.get(
#     'https://api.data.gov/ed/collegescorecard/v1/schools?fields=school.name,2016.cost.tuition.in_state&api_key=L0WwE8Ov5xU0IL6UYaw6rp1rZvDEqLzWT0IavjKi', verify=False)

# save the response as a file
# with open('./data/data.json', 'wb') as f:
