import mmap
# Test mmap.mmap code, derived from Michael Chui's web page:
#  http://www.cs.cmu.edu/~112/notes/notes-strings.html

def testStrings():
    startTime = time.time()
    f = open('frankenstein.txt')
    n = f.seek(0,2)
    str = f.read(n)
    f.close()
