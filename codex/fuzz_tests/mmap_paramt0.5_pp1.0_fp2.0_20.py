import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 'a'
    print m[0]
</code>
The output is ASCII 97, not ASCII 97, ASCII 10.


A:

I don't know what you mean by "the newline is added to the end of the file". But it sounds like you're expecting the file to contain <code>'a'</code> followed by a newline.
The code you posted doesn't do that. It writes a single byte to the file, the byte <code>0x01</code>. Then it opens the file again and replaces that byte with the byte <code>0x61</code>.
If you want to write a newline, you have to write a newline. You can do that by writing the string <code>'\n'</code> (which contains a single newline character), or by writing the bytes <code>b'\n'</code> (which contains a single newline byte).

