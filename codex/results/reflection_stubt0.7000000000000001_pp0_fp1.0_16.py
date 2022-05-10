fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# in case of memory error
import sys
sys.setrecursionlimit(10**9)

# in case of memory error
from scipy.sparse import csr_matrix as csr

# defaultdict
from collections import defaultdict
d = defaultdict(int)

# deque
from collections import deque
d = deque([], maxlen=10)

# bfs
from collections import deque
q = deque([(s, 0)])
while q:
    v, depth = q.popleft()
    for next_v in graph[v]:
        if next_v not in visited:
            visited.add(next_v)
            q.append((next_v, depth+1))

# bfs with priority queue
from heapq import heappush, heappop
q = [(0, s)]
while q:
    depth, v = heappop(q)
    for next_v in graph[v]:
        if next_v not in visited:
            visited.add(next_v)

