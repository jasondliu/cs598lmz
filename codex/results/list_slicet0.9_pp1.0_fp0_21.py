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
print len(keepali0e)
'''

print "case is normal"

def input():
    return """9
1 8
2 8
3 6
4 9
5 8
6 5
7 11
8 9
9 8
11
1 2
1 3
1 6
3 7
3 8
5 7
5 9
6 4
7 9
8 5
9 10"""

# setup
input = iter(input().splitlines())

#input
n = int(input.next())
levels = []
for _ in xrange(n):
    levels.append(map(int,input.next().split()))
m = int(input.next())
graph = [[] for _ in xrange(n+1)]
for _ in xrange(m):
    s,t = map(int,input.next().split())
    graph[s].append((t,levels[t-1][1]*levels[t-1][2]))

# do Dijkstra

seen = [0] # seen leel
que = heapq.heapify([
