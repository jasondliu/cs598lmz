import codecs
codecs.getreader('utf-8')(sys.stdin).readline()
def readline():
    r = sys.stdin.readline()
    if not r:
        return None
    if r[-1] == '\n':
        r = r[:-1]
    return r

D = readline()
if D is None:
    exit(0)
p1 = readline()
if p1 is None:
    exit(0)
p2 = readline()
if p2 is None:
    exit(0)

print p2
print " ".join(word[0] + ''.join(random.choice('oOf') for _ in range(len(word)-1))
                for word in p1.split())
