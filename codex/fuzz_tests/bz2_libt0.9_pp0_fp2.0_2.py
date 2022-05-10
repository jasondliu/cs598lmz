import bz2
bz2.decompress(all_data)
''' '.join(re.findall('[A-Z][^A-Z]*', all_data)) '''

f.close()

# unicode_string = 'strings and unicode'

# unicode_string.encode('utf-8')


# unique_characters = set(common_words)
# counts = []
# for char in unique_characters: counts.append((all_data.count(char), char))
# counts

# print(all_data.find('People'))

#print(all_data[221271:221271+10])

# print(3462/1233)


# def extract_info(string_list, string):
#     info_array = []
#     for s in string_list:
#         info_array.append(all_data.count(s))
#     return info_array

# print(extract_info(common_words, all_data))

# print(extract_info([c for c in set(common_
