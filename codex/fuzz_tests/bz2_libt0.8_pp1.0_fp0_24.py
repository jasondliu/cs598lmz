import bz2
bz2.decompress(f.read())

# f = gzip.open('../resource/asnlib/publicdata/project2-files-2018/train.json.gz')
df = json_normalize(json.loads(data), record_path='passages')
df.head(10)

# mydict = json.loads(data)
# mydict[1001]['query']

# with open('../resource/asnlib/publicdata/project2-files-2018/train.json', 'r') as f:
#     data = json.load(f)
#     for d in data:
#         print(d["query"])

# with open('../resource/asnlib/publicdata/project2-files-2018/train.json', 'r') as f:
#     for line in f:
#         data = json.loads(line)
#         for d in data:
#             print(d["query"])

# with open('../resource/asnlib/publicdata/project2-files-2018/train.json', 'r') as
