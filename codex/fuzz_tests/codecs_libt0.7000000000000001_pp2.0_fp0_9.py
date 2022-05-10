import codecs
codecs.open('hello.txt', 'w', encoding='utf8')

with codecs.open('hello.txt', 'w', encoding='utf8') as f:
    f.write('안녕하세요')

with codecs.open('hello.txt', 'r', encoding='utf8') as f:
    data = f.read()
    print(data)

# 여러 개의 파일을 열어서 읽은 다음 처리하고 싶을 때
# with문에 한번에 여러개의 파일을 지정해서 열어둘 수 있다.
with codecs.open('hello.txt', 'r', encoding='utf8') as f1, \
        codecs.open('hello
