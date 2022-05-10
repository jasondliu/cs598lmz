import threading
threading.stack_size(1000000)

def isprime(n):
  #print "in isprime function"
  if n == 1:
    return False
  if n == 2:
    return True
  for x in range(2, int(n**0.5)+1):
    if n % x == 0:
      return False
  return True

def primes(n):
  list = []
  for i in range(1, n+1):
    if isprime(i):
      list.append(i)
  return list

def main():
  primes(100000)
  
thread = threading.Thread(target=main)
thread.start()
