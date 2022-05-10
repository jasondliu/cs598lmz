from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bzip_compressed_as_bytes)

import threading

def input_numbers():
    res = []
    for i in range(5):
        num = int(input('Enter num: '))
        res.append(num)
    return res
def square_numbers():
    res = []
    for num in input_numbers():
        res.append(num*num)
    print('Result: ',res)
    
if __name__ == '__main__':
    t = threading.Thread(target=square_numbers)
    t.start()
    t.join()
