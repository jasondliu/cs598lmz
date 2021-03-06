import socket
socket.if_indextoname(7)
```
## 用Python实现magic_square
题目要求：
给定一个int[3][3]的数组，把数组重新排序，使得每一行的元素和相同，每一列的元素和相同，主对角线的元素和相同，副对角线的元素相同。

思路：
- 一个3*3的数组通过一次操作只能变成 [0, 8] <---> [2,6]
- 我们需要找到8次操作
