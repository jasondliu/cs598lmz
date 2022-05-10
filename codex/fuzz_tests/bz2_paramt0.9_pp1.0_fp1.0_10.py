from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"))

# coroutines

def grep(pattern):
    print("start searching for", pattern)
    try:
        while True: 
            line = yield  # принимаем строки
            if pattern in line:
                print(line)
    except GeneratorExit: 
        print("stop searching for", pattern)
    
ge = grep("python")
next(ge) # запустить генератор до получения первого значения
ge.send("python is the best") 
ge.send
