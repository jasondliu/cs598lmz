import socket
socket.if_indextoname(1)

print os.name
print sys.platform
print platform.system()
print platform.release()
print platform.version()
print os.getcwd()
print os.getpid()
print os.getlogin()
print os.getppid()
print os.times()
#os.symlink('/tmp/name','/haha/haha')
#os.mkfifo('/tmp/pid',0666)
# print sys.path #当前目录自动在最前
print os.listdir(os.getcwd())
for i in os.listdir(os.getcwd()):
    print i

print os.path.basename(__file__)
print os.path.dirname(__file__)
print os.path.split(__file__)
print os.path.dirname(os.path.dirname(__file__))

#os.system('cat /proc/cpuinfo |grep processor|wc -l')
# os.path.getsize('/etc
