import bz2
bz2.test()

# Example 2-11. Reading a compressed file
with bz2.open('lorem.txt.bz2', 'rt') as input:
    for line in input:
        print(line, end='')

# Example 2-12. Writing a compressed file
with bz2.open('lorem.txt.bz2', 'wt') as output:
    output.write(text)

# Example 2-13. Writing a compressed file in a single step
text = 'The same line, over and over.\n'
with bz2.open('lorem.txt.bz2', 'wt') as output:
    output.write(text * 1024)

# Example 2-14. Reading a compressed file in chunks
import bz2

with bz2.open('lorem.txt.bz2', 'rt') as input:
    for i, line in enumerate(input):
        if i == 10:
            break
        print(line)

# Example 2-15. Reading a compressed file in chunks
import bz2

with
