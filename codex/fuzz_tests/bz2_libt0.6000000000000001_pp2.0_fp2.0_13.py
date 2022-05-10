import bz2
bz2.open()
with bz2.open('test.bz2', 'rt', encoding='utf-8') as f:
    for line in f:
        print(line)

'''

'''
#zip
#zip은 경량의 압축 파일 포맷으로 여러 파일을 묶어 하나의 파일로 만들 수 있다.
#zip파일은 압축된 상태로 저장되므로 압축을 풀어야 한다.
#zipfile 모듈을 사용하면 zip파일을 생성하거나
