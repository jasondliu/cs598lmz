import lzma
# Test LZMADecompressor can run standalone.

with lzma.LZMADecompressor(format=lzma.FORMAT_XZ) as dec:
    with open('python-3.3.tgz', 'rb') as fp:
        data = fp.read(100)
        while data:
            decdata = dec.decompress(data)
            data = fp.read(100)
            if decdata:
                print(decdata)
</code>
But when I try to run it inside scrapy, I get this error:
<code>Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/scrapy/core/downloader/middleware.py", line 43, in process_request
    defer.returnValue((yield download_func(request=request,spider=spider)))
  File "/usr/local/lib/python3.4/dist-packages/twisted/internet/defer.py", line 382, in unwindGenerator
    return _inlineCallbacks(None, gen, Def
