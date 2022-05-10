from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
```

만약 이상적으로 진행된다면 위와 같은 출력값을 볼 수 있다. 만약 decompress 전에 print 시키면 bytes 형식으로 출력될 것이다. 이는 help(BZ2Decompressor) 시키면 볼 수 있다.

만약 decompress 한 결과가 “**b'Congratulations. You've successfully decompressed something compressed with bzip2.’” 이렇게 나오면 매우 좋은 시그
