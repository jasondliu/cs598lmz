import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a


def solve_small(N, J):
  #print(N, J)
  ret = []
  for x in range(2**(N-2)):
    str_x = bin(x)[2:].zfill(N-2)
    s = '1' + str_x + '1'
    factors = []
    for base in range(2, 11):
      num = int(s, base)
      factor = None
      for i in range(2, num):
        if num % i == 0:
          factor = i
          break
      if not factor:
        break
      factors.append(factor)
    if len(factors) == 9:
      ret.append((s, factors))
      if len(ret) == J:
        break
  return ret


def solve(N, J):
  return solve_small(N, J)


CASES
