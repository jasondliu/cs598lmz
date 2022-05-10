import codecs
codecs.register_error('replace_space', codecs.lookup_error('ignore'))
#reads the contents of a file as a string
def readex(fileName):
    f = open(fileName,'r', encoding='utf-8', errors='replace_space')
    return  f.read().rstrip('\n')
def get(regex, cont):
    m = re.search(regex, cont)
    return m.group(0)
def getAll(regex, cont):
    m = re.findall(regex, cont)
    return m
def case_length(case_name, x, y, z, w):
    print(case_name)
    print("Number of classes: %d" % (x))
    print("Number of interface: %d" % (y))
    print("Number of attributes: %d" % (z))
    print("Number of methods: %d\n" % (w))
# for(int i=0; i<something; i++)
# for(int i=0; i > something; i--)
def for_loop
