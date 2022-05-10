import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(lst)

#检查与验证
assert False, 'failed'

#调试
import random
import logging
random.seed(1)
logging.basicConfig(level=logging.DEBUG)
logging.debug('start program')
logging.debug('generate numbers')
for i in range(1,10):
    num=random.randint(1,10)
    if num==5:
        logging.debug("found num=%d"%num)
        break
logging.debug("program ended!")

import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('some debug information')
logging.info('some information')
logging.warning('some warning information')
logging.error('some error information')
logging.critical('some critical information')

#检查代码的健壮性
#assert条件语句
#logging模块
#python -O
