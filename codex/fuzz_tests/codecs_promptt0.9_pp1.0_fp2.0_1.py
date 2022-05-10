import codecs
# Test codecs.register_error('rollback', codec.ignore_errors)

f = open('1.txt')
hdr = codecs.lookup('gb2312')
codecs.register(lambda n: codecs.lookup('gb2312') if n == 'gb2312' else None)
result = codecs.open('result.txt', 'w')
for line in f:
    print >> result, line

print >> result, "abcdd"
f.close()
result.close()
