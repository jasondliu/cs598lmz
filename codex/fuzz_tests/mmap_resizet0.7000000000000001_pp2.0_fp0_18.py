import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>mmap.error: [Errno 22] Invalid argument</code>.


A:

The error is raised because you open the file in <code>r+b</code> mode, which means that the file is opened for updating (both for reading and writing). With <code>mmap.mmap</code> you can't open a file for updating, the documentation states: 
<blockquote>
<p>The mmap call creates a new mapping in the virtual address space of
  the calling process. The starting address for the new mapping is
  specified in <code>&lt;code&gt;addr&lt;/code&gt;</code>. The length argument specifies the length of the
  mapping. If <code>&lt;code&gt;length&lt;/code&gt;</code> is 0, the maximum length of the mapping will be
  the current size of the file when <code>&lt;code&gt;mmap&lt;/code&gt;</code> is called. <strong>The prot argument
  describes the desired memory protection of the mapping
