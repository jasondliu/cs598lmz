import lzma
lzma.open('test.txt.xz')

print(lzma.LZMAFile(open('test.txt.xz', 'r', encoding='utf-8'))) # text.txt.xz 파일을 읽어서
                                                                  # 압축을 푼후 콘솔창에 나타내는 예제
