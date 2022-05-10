import mmap
print "Hello, World"

#with open('pmid_pmc_ids.txt', 'r') as f:
#    mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
#    while True:
#        s = mm.readline().rstrip().split(' ')
#        print s

with open('pmid_pmc_ids.txt', 'r') as f:
    mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    for l in iter(mm.readline, ""):
        print l.rstrip().split(' ')
