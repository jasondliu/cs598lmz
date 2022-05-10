import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')

def valid(a,b,i,j,n,m,c,visited):
    if i>=0 and j>=0 and i<n and j<m and visited[i][j]!=1 and c[i][j]==1:
        return True
    return False

def BFS(x,y,n,m,o,c,visited):
    ini,mxx = [],[]
    maxx = 0
    q = []
    q.append([x,y])
    visited[x][y] = 1
    val = 0
    i=0
    j=0
    if c[x][y]==1 and o<4:
        val+=1
    #print(x,y,c[x][y])
    #print(val)
    while len(q)>
