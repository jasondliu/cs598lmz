from lzma import LZMADecompressor
LZMADecompressor().decompress(response.content)

# 이렇게 하면 데이터 크기가 너무 커져서 데이터 다운로드가 되지 않는다...
# 다른 방법을 찾는다.
# 서버를 호출하는 URL에 아래와 같이 range와 encoding을 적용해본다.
# range: bytes=0-4096
# encoding: gzip,x-gzip
# 인코딩을 사용하면 용량이 좀 더 줄어든다.
