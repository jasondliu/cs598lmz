import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
del a
del keepali0e
print(lst)
'''
'''
#问题:一道字符处理题十分复杂,线上执行消耗cpu明显高于线下,线上执行只有20条,线下执行到32w条时,问题待解决,
import time
def real_char_text(text):
    "match Chinese,English,number and blank. no /"
    import re
    for c in text:
        if re.match('[\u4e00-\u9fa5A-Z0-9\s]', c, re.IGNORECASE):
            yield c
        if c in "/": yield ' '
        
def real_char_test():
    real_char_text('中r  b中文 d中文   ')    

