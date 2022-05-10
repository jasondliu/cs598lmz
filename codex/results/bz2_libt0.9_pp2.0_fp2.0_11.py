import bz2
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084').decode('utf-8')

# level 9

from PIL import Image

im = Image.open('python_challenge_9.jpg')
pix = im.load()
w, h = im.size
print(w, h)
for x in range (w):
    for y in range(h):
        pix[x,y] = 255 - pix[x,y]
im.show()

# level 10

a = [1, 11, 21, 1211, 111221]

def f(n):
    return str(a[n])

n = 30
for i in range(1, n):
    a[0] = 1
    num_str = f(0
