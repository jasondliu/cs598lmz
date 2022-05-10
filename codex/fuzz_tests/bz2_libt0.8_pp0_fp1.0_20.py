import bz2
bz2_comp = bz2.BZ2Compressor()
data = open('test.img').read()
# 压缩方式一，按块压缩
count = 1
data_len = len(data)
i = 0
while i < data_len:
    c_data = bz2_comp.compress(data[i:i+1024])
    if c_data:
        open('test.img.bz2.'+str(count)+'.chunk', 'wb').write(c_data)
        i = i + 1024
        count += 1
        if count == int(data_len / 1024):
            c_data = bz2_comp.compress(data[i:])
            open('test.img.bz2.'+str(count)+'.chunk', 'wb').write(c_data)
    else:
        break
# 压缩方式二，一次性压缩
c_data = bz2_comp.compress
