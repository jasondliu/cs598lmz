import mmap
# Test mmap.mmap constructor argument
pos = 0
length = os.fstat(fileno).st_size
with mmap.mmap(fileno, length) as m:
    for line in m:
        print(line)
</code>
Here the same line "BEDROCK" from file gets printed twice:
<code>BEDROCK
BEDROCK
</code>
I want to know what the differences between these two methods and why the second method prints the same line twice.


A:

<code>mmap</code> doesn't work that way. What happens is:

you access <code>m</code>, an empty byte string;
<code>m</code> is replaced by the first line.

Hence on the first iteration you see the first line, and on the second iteration you see the same first line. (Don't be misled by the fact that the trailing newline is not included; it's still the same data.)
You can avoid the problem by writing the loop as:
<code>for line in m.splitlines():
    print(line)
</code>
so that the replacement of
