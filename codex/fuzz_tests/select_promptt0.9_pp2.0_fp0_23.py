import select
# Test select.select
print select.select([sys.stdin], [], [], 0)


print "Learning urllib"
# Test urllib
res = urllib.urlopen("http://www.baidu.com")
# Output the source code
print res.read()
