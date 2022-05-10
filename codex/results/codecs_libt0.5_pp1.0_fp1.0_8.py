import codecs
codecs.open('test.txt', encoding='utf-8')

# 바이너리 파일 읽기
with open('test.bin', 'rb') as f:
    data = f.read()

# 바이너리 파일 쓰기
with open('test.bin', 'wb') as f:
    f.write(b'Hello World')

# 텍스트 파일 읽기
with open('test.txt', 'rt') as f:
    data = f.read()

# 텍스트 파일 쓰기
with open('test.txt', 'wt') as f:
    f.write('Hello World')

# 바이너리 파일 읽기
with open('test.bin', 'rb') as f:
    data = f.read()
