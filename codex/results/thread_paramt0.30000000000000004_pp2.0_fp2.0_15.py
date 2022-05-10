import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1000000))))).start()
</code>
This is a simple script that starts a thread that prints out the numbers from 1 to 1,000,000. It works fine, but when I try to run it in the background, it doesn't work.
<code>$ python test.py &amp;
[1] 18777
</code>
I have to run it in the foreground to see the output.
<code>$ python test.py
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
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
