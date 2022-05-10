import mmap
# Test mmap.mmap using interned strings as keys.
msg = mmap.mmap(-1, 1024)
c1 = 'abc'
c2 = 'abcd'
c3 = 'abcde'
msg[c1] = c1
msg[c2] = c2
msg[c3] = c3
print msg[c1], msg[c2], msg[c3]
print msg.find(c1)
print msg.find(c2)
print msg.find(c3)

# Test mmap.mmap using non-interned strings as keys.
import string
msg = mmap.mmap(-1, 4096)
msg[string.lowercase] = string.lowercase
msg[string.uppercase] = string.uppercase
msg[string.digits] = string.digits
msg[string.punctuation] = string.punctuation
print string.lowercase
print msg.find(string.lowercase)
print string.uppercase
print msg.find(string.uppercase)
print string.digits
print msg.find(string.dig
