from lzma import LZMADecompressor
LZMADecompressor()
my_decompressor = LZMADecompressor()
my_decompressor.decompress(compressed_data)
my_decompressor.flush()

# write a file from a list
my_list = ['this is my list\n']
with open('my_list.txt', 'w') as list_file:
    for i in my_list:
        list_file.write(i)

# read a file into a list
with open('my_list.txt', 'r') as list_file:
    my_list = list(list_file)
print(my_list)

# write a file from a dict
my_dict = {'key1': 'value1\n', 'key2': 'value2\n'}
with open('my_dict.txt', 'w') as dict_file:
    for key in my_dict:
        dict_file.write(key + ':' + my_dict[key] + '\n')

# read a file into a dict
with open('my_dict.txt', 'r') as
