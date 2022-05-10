import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.b=weakref.ref(lst,callback)
print('\x83\x0c')
def hammingWeight(n):
    count=0
    while n:
        n&=n-1
        count+=1
    return count
if __name__=='__main__':
    print(hammingWeight(11))
