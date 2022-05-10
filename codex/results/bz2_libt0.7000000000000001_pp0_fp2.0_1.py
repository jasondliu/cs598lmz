import bz2
bz2.decompress(bz2_data)

def read_bz2(path):
    with bz2.open(path, 'rt') as file:
        for line in file:
            print(line)
read_bz2(path)


'''
【例2】
a = ['a', 'b', 'c', 'd']
b = list(range(1, 5))
c = []

with open('data.txt', 'w') as file:
    file.write('a b c d\n')
    file.write(str(a) + '\n')
    file.write(str(b) + '\n')
    file.write(str(c) + '\n')

with open('data.txt', 'r') as file:
    for line in file:
        print(line)

with open('data.txt', 'rb') as file:
    for line in file:
        print(line)
'''


'''
【例3】
with open('data.txt', 'a
