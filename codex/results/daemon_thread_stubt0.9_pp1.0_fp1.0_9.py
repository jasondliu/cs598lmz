import sys, threading

def run():
    cmd = 'ls *.txt>file.txt'
    os.system(cmd)

threading.Thread(target=run).start()

[root@server1 ~]# python test.py
[root@server1 ~]# ipython
Python 2.7.10 (default, May  6 2015, 16:30:39) 
Type "copyright", "credits" or "license" for more information.

IPython 2.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: for k in range(100):
   ...:     print k
   ...:     
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32

