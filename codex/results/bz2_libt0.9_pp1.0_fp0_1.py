import bz2
bz2file = bz2.BZ2File(infilename)

print "file %s opened, start reading..." % infilename
#chunk size
for i in xrange(0, 500000):
    print "start chunk[%d] reading..." % i
    d=bz2file.read(65536)
    if d == "":
        break
    params = dict()
    params['key']='fakekey'
    params['data']=bz2.compress(d)
    #print params
    print "start post..."
    r = requests.post('http://127.0.0.1:5600/parse/bulk2', data=params)
    print r
    print r.text


bz2file.close()
