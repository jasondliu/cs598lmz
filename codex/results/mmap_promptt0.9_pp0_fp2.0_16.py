import mmap
# Test mmap.mmap 内存映射版的 mmap.py for old py2
def test_mmap():
    teapot_uri = 'http://httpbin.org/stream-bytes/32768'    
    r = requests.get(teapot_uri, stream=True)
    url_fp = tempfile.NamedTemporaryFile()
    size = 0
    for chunk in r.iter_content(chunk_size=128):
        url_fp.write(chunk)
        size += len(chunk)
        print(chunk.encode('hex'), size)
    url_fp.seek(0)
    fp = mmap.mmap(url_fp.fileno(), size, prot=mmap.PROT_READ)
    #
    ans = 0
    while True:
        idx = fp.find('Coffee'.encode('utf-8'))
        if idx < 0:
            break
        ans += 1
        fp.seek(idx + 1)
    print('Coffee\'s count:',
