import bz2
bz2.BZ2File

import bz2

with bz2.BZ2File('example.bz2', 'w') as output:
    output.write(b"This is a compressed file.")

import bz2

with bz2.BZ2File('example.bz2', 'r') as input:
    print(input.read())

import bz2

with bz2.BZ2File('example.bz2', 'r') as input:
    print(input.readline())

import bz2

with bz2.BZ2File('example.bz2', 'r') as input:
    for line in input:
        print(line)

import bz2

with bz2.BZ2File('example.bz2', 'r') as input:
    for line in input:
        print(line.decode('ascii'))

import bz2

with bz2.BZ2File('example.bz2', 'r') as input:
    print(input
