from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b)

from zlib import decompress
decompress(b)

from bz2 import decompress
decompress(b)

## 5.3.3. 압축 해제 예외 처리하기
from bz2 import BZ2Decompressor

decompressor = BZ2Decompressor()

bz2_data = open('sample.bz2', 'rb').read()

try:
    data = decompressor.decompress(bz2_data)
except OSError as err:
    print('Not a valid bzip2 file:', err)

## 5.3.4. 압축 파일 읽기
import bz2

with bz2.open('sample.bz2', 'rt') as input:
    for line in input:
        print(line.rstrip())

## 5.3.5. 압축 파
