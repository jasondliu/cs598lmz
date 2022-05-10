import lzma
lzma.decompress(b'\xfd...')

zipfile.ZipFile(open('example.zip', 'rb'))

#字典解包
d = dict(query='zhangsan', age='31', sex='male', nation='china')
get_name(**d)
def get_name(query, age, sex='female', nation='china'):
    print(query)
    print(age)
    print(sex)
    print(nation)

print('abc', end='') #python3, no newline and space
print('abc')

#位置参数、关键字参数和可变参数
#位置参数：在调用时传入的值会自动关联到福禄择置参数上面。
#关键字参
