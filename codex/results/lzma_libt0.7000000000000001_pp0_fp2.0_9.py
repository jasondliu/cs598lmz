import lzma
lzma.decompress(lzma_data)

# lzma_data 는 이미 문자열 형태의 데이터기 때문에 open('filename', 'rb') 과 같은 처리를 하지 않아도 된다.

# 만일 바이너리 데이터를 디코딩 한 뒤에 출력해야한다면 아래와 같이 처리 할 수 있다.

print(lzma.decompress(lzma_data).decode('utf-8'))


# 파일 객체
