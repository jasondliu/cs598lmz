import mmap
# Test mmap.mmap



addr,piper,pipec=comm.get_pipe_info(0)	
comm.connect(addr,piper,pipec)

f=open("../../sample/hello.txt",'rb')

data=mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

retcode=comm.write_full(data[0:8])

assert(retcode==8)




data=comm.read_all()
print("returned {} bytes".format(data))
print(data)

assert(data==b"hello mmap")





#
#result = exec_program("../../simple_tests/mbuffer 1024 1024"
#	,stdout_read=True,stdout_show=True,stderr_show=True)
#
#assert(status_of(result)==0)
#
