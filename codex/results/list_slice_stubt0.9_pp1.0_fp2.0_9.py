import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
keepali0e.append(a)
a=None
for i in keepali0e:
    print(i)
    print(i.c)
    

def example14():
    s=100
    a=WeakKeyDictionary()
    a[s]='100'
    print(a[s])
    del s
    gc.collect()
    print(a)

import bisect
def excercise():
    def make_word_list1():
        t=[]
        fin = open('../Resources/words.txt')
        for line in fin:
            word = line.strip()
            t.append(word)
        return t
    def make_word_list2():
        t=[]
        fin = open('../Resources/words.txt')
        for line in fin:
            word = line.strip()
            t=t+[word]
        return t

    start_time1=time.time()
    t=make_word_list1()
    bis
