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
del lst
del keepali0e

def main():
    array = Array(Size)
    for i in range(1, Size):  # 用 1 到 Size 依次填入数组
        array[i] = i

    while array.count():  # 当数组中还存在数字时
        i = randrange(1, array.count() + 1)  # 随机取出其中任意一个乘征
        j = randrange(1, array.count() + 1)  # 随机取出其中任意一个数字
        array.swap(i, j)  # 将这两个数字交换

    for i in range(1, Size):
        print(array[i], end=' ')  # 依次输出 1 到 Size

