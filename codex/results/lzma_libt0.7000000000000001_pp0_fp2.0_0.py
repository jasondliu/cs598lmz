import lzma
lzma.open('lorem.xz')

class MyXzFile(lzma.LZMAFile):
    def __init__(self, file, mode):
        super().__init__(file, mode)
        # Custom initialization

lzma.register_open('xz', MyXzFile)
lzma.open('lorem.xz')
</code>

