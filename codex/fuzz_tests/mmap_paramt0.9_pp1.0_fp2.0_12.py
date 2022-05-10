import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print('bytearray(m):', bytearray(m))
    print('str(m)', str(m))
    print('m.read(3):', [m.read(3)])
</code>
The results are:
<code>bytearray(m): bytearray(b'\x00')
str(m): b'\x00'
m.read(3): [b'\x00']
</code>
As you can see, the file I created and the text from <code>bytearray</code> and <code>str</code> are all the same, but byte <code>\x00</code> read from memory map is different than byte <code>\x00</code> itself, which causes problem for my program. So anyone can explain what is happening, and how can I fix it?


A:

You didn't even open your file in text mode, so your file cannot contain text, meaning characters like <code>\n</code> or <code>\t</code>.
The file content is a single <code>
