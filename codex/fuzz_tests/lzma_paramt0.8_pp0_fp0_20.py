from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_compressed_string)
# '압축이 풀리는지 확인합니다.'
```

## `.decompress(data)`

입력받은 데이터를 압축 해제한 후 반환합니다.

압축된 데이터는 일반적으로 저장된 파일의 형태인 `bytes` 타입을 입력받습니다.

아래의 예시에서는 압축된 데이터
