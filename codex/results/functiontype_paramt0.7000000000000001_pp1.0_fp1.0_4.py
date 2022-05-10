from types import FunctionType
list(FunctionType(1,2,3,4,5,6,7,8))

## 2.5
## 从键盘输入一个整数，然后输出其二进制表示中1的个数。
## >>> b = int(input('input a number:'))
## input a number:3
## >>> a = bin(b)[2:]
## >>> print(a)
## 11
## >>> c = a.count('1')
## >>> print(c)
## 2

## 2.6
## 写一个函数，接受一个list作为参数，统计list中每个元素出现的次数，返回一个dict。
## 比如：
## l = [1,1,1,2,2,3,3,3,3,4
