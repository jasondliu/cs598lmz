import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
#

#
# for file in os.listdir('./Data/Train/'):
#     print(file)
#     with open('./Data/Train/'+file, 'r', encoding='utf8') as f:
#         for line in f:
#             print(line)
#             break
#     break
#
#
#
# with open('./Data/Train/train_data_0.json', 'r', encoding='utf8') as f:
#     for line in f:
#         print(line)
#         break
#
#
#
#
# with open('./Data/Train/train_data_0.json', 'w', encoding='utf8') as f:
#     f.write('json_data')
#
#
#
# with open('./Data/Train/train_data_0.json', 'r', encoding='utf8') as f:
#     for line in f:
