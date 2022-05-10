import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 48
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
The output is <code>b'0'</code>, which shows that the file has been changed. 
However, when I try to do the same thing using Visual Studio Code and Python 3.7.2 64-bit, I get <code>b'\x01'</code>.
I have tried the following things without any luck:

Setting the file encoding to <code>utf-16le</code>
Using Python 3.6.7 64-bit
Using the Python extension in VS Code
Adding the following line to <code>settings.json</code> in the workspace: <code>"files.encoding": "utf-8"</code>

The only thing that actually works is running the script from a terminal.
Is there some setting in VS Code that I need to change to get this to work?

