import mmap
# Test mmap.mmap() for a file descriptor
result = mmap.mmap(-1, os.fstat(fd).st_size, mmap.MAP_PRIVATE, mmap.PROT_WRITE, fd)
# Test mmap() for a path
result = mmap.mmap(fd, os.fstat(fd).st_size, mmap.MAP_SHARED, mmap.PROT_WRITE)
'''
def run(filename):
    prog = tidb_cfg.run_cmd(tidb_cfg.node1_ip, tidb_cfg.tidb_port, "select @@version_comment limit 1;")
    res = os.popen(prog).readlines()
    comment = res[0]
    print(filename, 'test:', comment)

    fd = os.open(filename, os.O_RDONLY)
    mmap_mode = [
            [mmap.PROT_WRITE, mmap.MAP_PRIVATE],
            [mmap.PROT_WRITE, mmap.MAP_PRIVATE|
