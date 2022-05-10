import lzma
lzma.path = r'/.nvm/versions/node/v13.3.0/bin/xz'  # path for custom lzma
lzma.lzma_compress = lambda data: subprocess.check_output([lzma.path, '-9z', '-c', '-'],
                                                    input=data.encode())
lzma.lzma_decompress = lambda data: subprocess.check_output([lzma.path, '-c', '-d', '-'],
                                                      input=data).decode()
</code>
However I'm getting the following error:
<code>lzma.Decompressobj().decompress(data)
FileNotFoundError: [Errno 2] No such file or directory: '/.nvm/versions/node/v13.3.0/bin/xz': '/.nvm/versions/node/v13.3.0/bin/xz'
</code>
I can print <code>r'/.nvm/versions/node/v13.3.0
