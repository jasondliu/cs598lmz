import bz2
bz2.BZ2File
file = bz2.BZ2File(r"D:\code\python\python_learning\scrapy\scrapy_test\scrapy_test\data\我不是药神.html.bz2")
type(file)

data = file.read()

data

data = data.decode('utf-8')

data
