import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be <code>bytes(1)</code>, but instead it is <code>bytes(0)</code>. Why doesn't the mmap persist after the file was truncated?


A:

<blockquote>
<p>Why doesn't the mmap persist after the file was truncated?</p>
</blockquote>
From the <code>mmap</code> docs:
<blockquote>
<p>On UNIX, <code>&lt;code&gt;mmap&lt;/code&gt;</code> operations on files may not be compatible with other types of access, such as <code>&lt;code&gt;read&lt;/code&gt;</code>, <code>&lt;code&gt;write&lt;/code&gt;</code>, and <code>&lt;code&gt;seek&lt;/code&gt;</code>. On Windows, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> and file operations are completely independent, and can
