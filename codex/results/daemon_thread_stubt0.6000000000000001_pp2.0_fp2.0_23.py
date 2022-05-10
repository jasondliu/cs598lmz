import sys, threading

def run():
    for i in range(1, 100):
        sys.stdout.write("%d\n" % i)

thread = threading.Thread(target=run)
thread.start()

for i in range(1, 100):
    sys.stdout.write("%d\n" % i)
</code>
However, the results I get are not as expected. I get output like this:
<code>1
2
3
4
5
6
7
8
9
10
1
11
12
13
14
15
16
17
18
19
1
20
21
22
23
24
25
26
27
28
1
29
30
31
32
33
34
35
36
37
1
38
39
40
41
42
43
44
45
46
1
47
48
49
50
51
52
53
54
55
1
56
57
58
59
60
61
62
63
64
1
65
66
67
68
69
70
71

