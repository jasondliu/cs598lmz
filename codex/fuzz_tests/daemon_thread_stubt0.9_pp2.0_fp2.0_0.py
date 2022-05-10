import sys, threading

def run():
  while True:
    assert False

def main():
  t = []
  for i in xrange(50):
    t.append(threading.Thread(target=run))
    t[-1].start()
    print 'Thread ', i
  [i.join() for i in t]

if __name__ == '__main__':
  main()
</code>
Output:
<code>Thread  0
Thread  1
Thread  2
Thread  3
Thread  4
Thread  5
Thread  6
Thread  7
Thread  8
Thread  9
Thread  10
Traceback (most recent call last):
Thread  11
Thread  12
Thread  13
Thread  14
Thread  15
Thread  16
Thread  17
Thread  18
Thread  19
Thread  20
Thread  21
Thread  22
Thread  23
Thread  24
Thread  25
Thread  26
Thread  27
Thread  28
Thread  29
Thread  30
Thread  31
Thread  32
Thread  33
Thread  34
Thread  35
Thread  36
