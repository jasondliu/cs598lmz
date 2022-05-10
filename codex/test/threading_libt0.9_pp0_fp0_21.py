import threading
threading.stack_size(2**12)

def gettime():
    
    t = time.time()
    return str(t)

def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, str) else 2 if isinstance(src, bytes) else 0
    for i in range(0, len(src), length):
        chars = src[i:i+length]
        hex = ' '.join(["{0:{1}x}".format(c, digits) for c in chars])
        text = ''.join([chr(c) if 0x20 <= c < 0x7F else '.' for c in chars])
        result.append("{0:04x}   {1:<{2}}   {3}".format(i, hex, length*(digits + 1), text))
    return '\n'.join(result)

def convertstring(hexdump, start, length):
    mylist = []
    index = start*3
