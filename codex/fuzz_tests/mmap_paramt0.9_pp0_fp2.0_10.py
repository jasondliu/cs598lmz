import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)

    # Increment by one the first byte
    m[0] = ord(m[0:1]) + 1

    m.close()
</code>
This works as expected, however when I do the same in <code>test.c</code>
<code>#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;
#include &lt;fcntl.h&gt;
#include &lt;sys/mman.h&gt;

int main(void) {
    FILE* fp = fopen("test", "r+b");
    if(fp == NULL) {
        printf("fopen failed");
        exit(1);
    }
    void* map;
    if ((map = mmap(0, 2, PROT_READ|PROT_WRITE, MAP_SHARED, fileno(fp), 0)) == (void *)-1) {
        perror("mmap");
        exit(1);
    }
    printf("%c\n", *(char *
