import bz2
bz2_file = bz2.BZ2File('text.bz2', mode='w')
bz2_file.write(text)
bz2_file.close()
with open('text.bz2', mode='rb') as f:
    print(f.read().decode('utf-8'))

print('\n'+'='*50+'\n')

import gzip
with gzip.open('text.gz', mode='wb') as f:
    f.write(text.encode('utf-8'))

with gzip.open('text.gz', mode='rb') as f:
    print(f.read().decode('utf-8'))

print('\n'+'='*50+'\n')

import zipfile
with zipfile.ZipFile('text.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as z:
    z.write('text.txt')

with zipfile.ZipFile('text.zip', mode='r') as z:
    for name in z
