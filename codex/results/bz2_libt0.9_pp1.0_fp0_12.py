import bz2
bz2.BZ2Decompressor().decompress(b_x)

re.findall("\\bAllosaur\\b", s)
re.findall('\\b(?:Allosaur)\\b', s) # non capturing group
print(re.findall('\\b(?:Allosaur)\\b', s)) # don't print 

s = "Three dinosaurs: Allosaurus and pterodactyls and triceratops"
req1 = "r"
rep1 = "%r"
req2 = "p"
rep2 = "%p"
req3 = "u"
rep3 = "9"
req4 =  "o"
rep4 = "0"
print(re.sub(req1, rep1, s))

def foo(m):
  return "%s%%s%s%%s%s%%s%s%%s" % (m.groups()[0],m.groups()[1],m.groups()[2],m.groups()[3])
  #return repeater % (m.group(1),m.group(2),m
