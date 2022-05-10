import bz2
bz2.BZ2File('data.json.bz2', 'w')

with bz2.BZ2File('data.json.bz2', 'w') as f:
    f.write(json.dumps(data))

with bz2.BZ2File('data.json.bz2', 'r') as f:
    print(f.read())

# save json file with gzip
import gzip
f = gzip.open('data.json.gz', 'wt')
json.dump(data, f)
f.close()

with gzip.open('data.json.gz', 'rt') as f:
    print(f.read())

# save json file with zipfile
import zipfile
zip = zipfile.ZipFile('data.zip', 'w', zipfile.ZIP_DEFLATED)
zip.write('data.json', compress_type=zipfile.ZIP_DEFLATED)
zip.close()

zf = zipfile.ZipFile('data.zip')
data = json.loads(zf.read
