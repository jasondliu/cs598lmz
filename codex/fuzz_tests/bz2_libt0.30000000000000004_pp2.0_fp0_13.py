import bz2
bz2.BZ2File('./data/train.ft.txt.bz2')

# 파일을 읽어온다.
with bz2.BZ2File('./data/train.ft.txt.bz2') as f:
    raw_data = f.readlines()

# 파일을 읽어온 데이터의 개수를 확인한다.
print(len(raw_data))

# 파일을 읽어온 데이터 중 첫 번째 데이터를 확인한다.
print(raw_data[0])

# 파일을 읽어온 데이터 중 마지막
