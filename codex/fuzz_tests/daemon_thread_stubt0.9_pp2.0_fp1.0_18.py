import sys, threading

def run():
    global f, p
    cmd = 'cp {}/{} ./{}'.format(sys.argv[1], p, f)
    print(cmd)
    os.system(cmd)
    cmd = 'python3 analyzemaps.py %s %s' % (p, len(newclusters))
    print(cmd)
    os.system(cmd)
    cmd = 'mv *.png {}/%s'.format(sys.argv[2]) % p
    print(cmd)
    os.system(cmd)
    #cmd = 'mv *.gif {}/%s'.format(sys.argv[2]) % p
    #print(cmd)
    #os.system(cmd)

files = sys.argv[3]
with open(files) as f:
    files = f.readlines()
files = [x.strip() for x in files]   

newclusters = map(lambda f: (f.split('-')[2], f), files)
newclusters = sorted(newclusters, key = lambda x: int(
