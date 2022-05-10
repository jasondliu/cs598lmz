import sys, threading

def run():
  infile = open(sys.argv[1])
  outfile = open(sys.argv[2], 'w')
  for line in infile:
    (f, h) = line.split()
    r = subprocess.call([sys.argv[3], f, f+'.out'])
    if r == 0:
      if filecmp.cmp(f+'.out', h):
        outfile.write('%20s   OK\n' % f)
      else:
        outfile.write('%20s   FAIL\n' % f)
    else:
      outfile.write('%20s   ERROR: exit code=%d\n' % (f, r))
  exit(0)

thr = threading.Thread(target=run)
thr.start()
thr.join(float(sys.argv[4]))

if thr.isAlive():
  os.kill(os.getpid(), signal.SIGKILL)
  raise RuntimeError('Timeout')
