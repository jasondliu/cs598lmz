import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The above code does the equivalent of the following C code.
<code>#include &lt;unistd.h&gt;
#include &lt;sys/mman.h&gt;

int main(){
    int fd = open("./test.txt", O_RDWR|O_TRUNC);
    ftruncate(fd, 0);
    char *m;
    m = mmap(0, 1, PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0);
    char a = *m;
    printf("%c", a);
}
</code>
The C equivalent works as expected and produces an exit code of <code>136</code>. The python code fails during the truncate call with the following message:
<code>OSError: [Errno 22] Invalid argument
</code>
Is there a way to make this code run in python, or is there a better way to do what I want to do?

FWIW, I'm using ExtendPython and all the code was adapted from Extend
