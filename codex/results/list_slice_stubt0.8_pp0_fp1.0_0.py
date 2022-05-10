import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
a.fn=callback
keepalive.append(a)
lst[0]="hello world"
with open('test.pickle','wb') as f:pickle.dump(lst,f,pickle.HIGHEST_PROTOCOL)
with open('test.pickle','rb') as f:lst=pickle.load(f)

```

> 作者：陈博
>
> 来源：CSDN
>
> 原文：https://blog.csdn.net/calvin1985/article/details/79573427
>
> 版权声明：本文为博主原创文章，转载请附上博文链接！
