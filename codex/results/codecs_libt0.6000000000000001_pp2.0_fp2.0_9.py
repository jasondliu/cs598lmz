import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# def get_data(filename):
#     data = []
#     with open(filename, 'r', encoding='utf-8') as f:
#         for line in f:
#             data.append(line.strip().split('\t'))
#     return data

def get_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split('\t')
            line[3] = int(line[3])
            line[4] = int(line[4])
            line[5] = int(line[5])
            line[6] = int(line[6])
            line[9] = int(line[9])
            line[10] = int(line[10])
            line[11] = int(line[11])
            line[12] = int(line[12])
            data.append
