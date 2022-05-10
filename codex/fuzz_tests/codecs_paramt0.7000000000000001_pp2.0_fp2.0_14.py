import codecs
codecs.register_error('strict', codecs.ignore_errors)

nameList = [u'令狐冲']

file = open('./test.txt', 'w')
file.write('\n'.join(nameList).encode('GBK', 'strict'))
file.close()

import os

os.system('chcp 65001')

print('\n'.join(nameList).encode('GBK', 'strict'))

print('\n'.join(nameList).encode('GBK', 'strict').decode('GBK'))

print('\n'.join(nameList).encode('GBK', 'strict').decode('GBK').encode('utf-8').decode('utf-8'))

print('\n'.join(nameList).encode('GBK', 'strict').decode('GBK').encode('utf-8'))

# print('\n'.join(nameList).encode('GBK', 'strict').decode('GBK').encode('utf-8').decode('
