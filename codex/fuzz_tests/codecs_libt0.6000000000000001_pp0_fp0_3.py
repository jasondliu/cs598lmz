import codecs
codecs.open('d:\\1.txt','w','cp1251')

import sys
print(sys.stdout.encoding)
print(sys.getdefaultencoding())
sys.stdout = codecs.getwriter('cp866')(sys.stdout)
print('привет')
print(sys.stdout.encoding)
sys.stdout = codecs.getwriter('cp1251')(sys.stdout)
print('привет')
print(sys.stdout.encoding)

import sys
print(sys.stdout.encoding)
sys.stdout = codecs.getwriter('cp866')(sys.stdout)
print('привет')
print(sys.stdout.encoding)
sys.stdout = codecs.getwriter('cp1251')(sys.stdout)
print('привет')
print(sys.stdout.encoding)

import sys
print(sys.stdout.encoding)
sys.stdout = codecs.get
