import mmap
# Test mmap.mmap
_testcode = '''
import mmap
f = open("_pytest/test_mmap.txt", "w")
f.write("1234567890")
f.close()

f = open("_pytest/test_mmap.txt", "r+")
m = mmap.mmap(f.fileno(), 10)

a = m.find("123")
m[a] = "abc"
b = m[a:a+3]

f.close()
m.close()
'''

def test_mmap1():
    import mmap
    f = open("_pytest/test_mmap.txt", "w")
    f.write("1234567890")
    f.close()
    
    f = open("_pytest/test_mmap.txt", "r+")
    m = mmap.mmap(f.fileno(), 10)
    
    a = m.find("123")
    m[a] = "abc"
    b = m[a:a+3]

