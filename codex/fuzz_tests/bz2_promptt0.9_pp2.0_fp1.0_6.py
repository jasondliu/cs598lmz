import bz2
# Test BZ2Decompressor is working.
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BBP\x91\xf08'
bz2.decompress(data)

file = bz2.BZ2File('data/degrees.json.bz2')

data = []

for line in file:
    data.append(json.loads(line))
    
degrees = data
len(degrees)

def count_majors(degrees):
    degree_count = {}
    for d in degrees:
        if d['major'] in degree_count:
            degree_count[d['major']] += 1
        else:
            degree_count[d['major']] = 1
    for key in degree_count:
        degree_count[key] = degree_count[key]/len(degrees)*100

