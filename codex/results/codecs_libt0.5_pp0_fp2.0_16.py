import codecs
codecs.lookup('utf-8')

# 파일 이름을 지정하고, 그것을 변수에 저장한다.
file_name = 'hong.txt'

# 파일을 읽기 모드로 연다.
file = open(file_name, 'r')

# 파일의 내용을 읽어서 변수에 저장한다.
file_contents = file.read()

# 파일을 닫는다.
file.close()

# 파일의 내용을 출력한다.
print(file_contents)

# 파일을
