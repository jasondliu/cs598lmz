import bz2
bz2.compress(b'i am a string')

#bz2.compress(b'i am a string')


#1.2 前面的字符串是bytes类型，所以在前面加了一个b，要是字符串本身包含的就是bytes，那就不用再加了。
#2.1 压缩后的数据都是bytes类型的，要想打印出来，就需要用decode()方法；
#2.2 压缩的值可以保存到文件中，直接用open()方法即可。

#compress()方法返回的就是一
