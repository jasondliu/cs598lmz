import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=str()
a.e=str()
c=weakref.ref(a,callback)#类似于a.__del__=callback
def main():
    # del keepalive
    # del a
    # del lst
    # print(a)
    while True:
        print(a)
        time.sleep(0.2)

if __name__ == '__main__':
    main()
