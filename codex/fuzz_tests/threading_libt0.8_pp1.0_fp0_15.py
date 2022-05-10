import threading
threading.stack_size(2**27)
sys.setrecursionlimit(10**5)

def main():
   input = sys.stdin.readline
   def readints():
      return list(map(int, input().strip().split()))
   def readint():
      return int(input().strip())
   def readstrs():
      return list(input().strip().split())
   def readstr():
      return input().strip()
   t = readint()
   for _ in range(t):
      N = readint()
      if N == 1:
         print(1)
      elif N == 2:
         print(11)
      else:
         res = [1]
         for i in range(N-1):
            res.append(1)
         res[0] = 2
         res[1] = 1
         for i in range(3, N):
            res[i-1] = (res[i-2] * 11) % 1000000007
         s = "".join([str(x) for x in res])
         print
