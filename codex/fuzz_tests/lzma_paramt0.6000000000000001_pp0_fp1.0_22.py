from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# b'This is the original text.'

# io.BytesIO 클래스는 메모리 기반의 바이트 배열을 가지는 파일처럼 동작하는 스트림 객체를 만들어 준다.
# 메모리 기반의 스트림은 소켓이나 기타 장치에 의존하지 않기 때문에 스트림을 직접 작업하는 
