import codecs
codecs.register_error("ignore", codecs.replace_errors)

# 返回一个字典
def get_dictionary(path):
    dictionary = dict()
    with codecs.open(path, 'r', 'utf-8') as f:
        for line in f:
            word, freq = line.split()
            dictionary[word] = int(freq)
    return dictionary

# 返回一个字典，对应的键值对为dict[word] = id
def get_reverse_dictionary(path):
    dictionary = dict()
    with codecs.open(path, 'r', 'utf-8') as f:
        for index, line in enumerate(f):
            word, freq = line.split()
            dictionary[word] = index
    return dictionary

# 用于生成一个词典，将文本转化为id序列
# 参数：

