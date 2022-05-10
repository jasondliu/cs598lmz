import bz2
bz2_file = bz2.BZ2File('/Users/jiankaiwang/Desktop/data/wiki-en-text.txt.bz2')
data = bz2_file.readlines()
data = [x.decode('utf-8') for x in data]
data = [x.strip() for x in data]
data = [re.sub('=\n', '', x) for x in data]
data = [re.sub('<.*>', '', x) for x in data]
data = [re.sub('\(.*\)', '', x) for x in data]
data = [x for x in data if x]
data = [x for x in data if not x.startswith('=')]
data = [x for x in data if not x.startswith('<')]
data = [x.split() for x in data]
data = [x for x in data if x]
data = [x for x in data if len(x) >= 5]
data = [x for x in data if len(x) <= 25]

