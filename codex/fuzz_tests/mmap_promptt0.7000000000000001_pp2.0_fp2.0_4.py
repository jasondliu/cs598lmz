import mmap
# Test mmap.mmap(0, 1, "", mmap.MAP_SHARED, 0, 0) and
# mmap.mmap(0, 1, "", mmap.MAP_SHARED | mmap.MAP_ANONYMOUS, 0, 0)

# The C code looks like this:
#  #include <sys/mman.h>
#  int main(int argc, char *argv[]) {
#    char *buf;
#    buf = mmap(0, 1, PROT_READ|PROT_WRITE, MAP_SHARED, 0, 0);
#    if (buf == MAP_FAILED)
#      exit(1);
#    buf[0] = 'a';
#    munmap(buf, 1);
#    buf = mmap(0, 1, PROT_READ|PROT_WRITE, MAP_SHARED|MAP_ANONYMOUS, 0, 0);
#    if (buf == MAP_FAILED)
#      exit(1);
#    buf[0] = 'b';
#    munmap(buf
