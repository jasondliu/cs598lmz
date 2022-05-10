import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 迭代器
import itertools as it
it.count(1)

# 可索引的迭代器
alist = [1,2,3,4,5,6]
it.islice(alist,3,5)

# 排列组合
it.permutations(range(3))
it.combinations(range(4),2)
list(it.product(range(3),repeat=2))
