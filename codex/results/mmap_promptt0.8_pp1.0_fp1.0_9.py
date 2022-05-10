import mmap
# Test mmap.mmap.  
import corebio.seq_io
import corebio.DNA
def test_mmap():
    f = corebio.seq_io.SequenceInputStream(corebio.DNA.AmbiguousDNA.IUPAC,
                                           't/data/toy.fasta',
                                           't/data/toy.fastq')
    for s in f:
        break
        print s   
    f = open('t/data/toy.fasta','r')
    d = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    e = d[:]
    print e
    assert e == s.data, "Read string %s != expected %s" % (e,s.data)
