import io
# Test io.RawIOBase.readall
print (io.RawIOBase.readall.__doc__)

with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

