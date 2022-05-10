import bz2
bz2.decompress(
    b'BZh91AY&SY\xc4\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
)
print("done")

#unzipping the file
import gzip
with gzip.open('pycharm.html.gz', 'rb') as f:
    file_content = f.read()
    print(type(file_content))
    with open('pycharm.html', 'wb') as f:
        f.write(file_content)
print("done")
