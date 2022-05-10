from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<I'
s.size = 4
os.lstat('/etc/passwd')
os.readlink('/etc/passwd')  # ==> '/etc/pwdb'
os.remove('/tmp/somefile')
os.rename('/etc/hosts', '/etc/hosts.old')
os.system('vi hello.py')
os.tmpfile()
os.tmpnam()
os.ttyname(0)
os.ttyname(1)
os.ttyname(2)
os.ttyname(3)
pwd.getpwuid(os.geteuid())[0]
pwd.getpwuid(os.getuid())[0]
random.seed()
random.random()
random.uniform(a, b)  # <==> a + (b-a)*random()
random.getrandbits(k)
random.randrange(start, stop=None, step=1)
random.sample(population, k)
random.choice(seq)
