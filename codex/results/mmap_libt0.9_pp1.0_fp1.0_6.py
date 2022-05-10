import mmap

contents = ''
with open('./randomNum.txt', 'r+') as f:
    # memory-map the file, size 0 means whole file
    map = mmap.mmap(f.fileno(), 0)
    data = map.read()
    #print(data)
    for line in data.splitlines():
        contents=contents+ 'a'+line+'b'

    print(contents)
