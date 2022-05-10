import bz2
bz2.decompress(bz2.compress(str(range(10000))))

# 字符串格式化
print('%s, eggs, and %s' % ('spam', 'SPAM!'))
'{0}, eggs, and {1}'.format('spam', 'SPAM!')
'{}, eggs, and {}'.format('spam', 'SPAM!')
'{:,.2f}'.format(296999.2567)
'%.2f | %+05d' % (3.14159, -42)

# 文件
f = open('data.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.close()

f = open('data.txt')
text = f.read()
text

text.split()

dir(f)

f.seek(0)

f.readline()

f.readline()

f.readline()

f.seek(0)

list(f)


