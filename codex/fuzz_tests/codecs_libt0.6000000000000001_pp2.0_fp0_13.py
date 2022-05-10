import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 파일 읽기
file = open("data/example.txt", "r", encoding="UTF-8")

# 파일 읽기
# file = codecs.open("data/example.txt", "r", encoding="UTF-8")

# 파일 읽기
# file = open("data/example.txt", "r", encoding="UTF-8")

# 데이터 전체 읽기
data = file.read()
print(data)

# 데이터 줄단위 읽기
# line = file.readline()
# print(line)

# 데이터 닫기
file.close()
