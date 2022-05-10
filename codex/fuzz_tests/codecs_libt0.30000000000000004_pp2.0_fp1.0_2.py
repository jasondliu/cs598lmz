import codecs
codecs.open('test.txt', 'r', 'utf-8')

# 파일 읽기
f = codecs.open('test.txt', 'r', 'utf-8')
text = f.read()
print(text)
f.close()

# 파일 쓰기
f = codecs.open('test.txt', 'w', 'utf-8')
text = '안녕하세요'
f.write(text)
f.close()

# 파일 읽기
f = codecs.open('test.txt', 'r', 'utf-8')
text = f.read()
print(text)
f.close()

# 파일 쓰기
f = codecs.open('test.txt', 'w', 'utf-8')
text = '안녕하세요'
f.write(text)
f.close()

# 
