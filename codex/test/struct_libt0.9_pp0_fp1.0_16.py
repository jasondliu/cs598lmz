import _struct
from timeit import default_timer as timer
from multiprocessing import Pool


# this generates a + 0, b + 0, c + njk, d + njk
def generate_dict(j, k, l):
	item_in_jk = k * j
	dic = {}
	for i in range(l):
		dic[chr(i + 97) + ' + 0'] = ['add', i, 0]
		dic[chr(i + 97) + ' + ' + str(item_in_jk)] = ['add', i, item_in_jk]
	return dic

# this generates a + i, b + i, c + njk + i, d + njk + i
def generate_dict2(j, k, l):
	item_in_jk = k * j
	dic = {}
	for i in range(l):
		dic[chr(i + 97) + ' + ' + str(i)] = ['add', i, i]
		dic
