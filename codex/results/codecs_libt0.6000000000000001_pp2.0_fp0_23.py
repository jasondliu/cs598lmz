import codecs
codecs.open('test.txt', 'r', 'utf-8')

# 파일을 읽기 모드로 열고 인코딩을 UTF-8로 설정한다.
# 이후 읽어온 파일은 문자열로 저장한다.
f = codecs.open('test.txt', 'r', 'utf-8')
lines = f.readlines()
f.close()

# 파일을 쓰기 모드로 열고 인코딩을 UTF-8로 설정한다.
# 이후 지정한 내용을 기록한다.
f =
