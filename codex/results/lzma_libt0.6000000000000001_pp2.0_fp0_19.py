import lzma
lzma.LZMAError: Cannot allocate memory
</code>
I'm not sure what's going wrong here. Any ideas?


A:

<code>lzma</code> is a low-level wrapper around liblzma, and it's documented that <code>LZMAError</code> is thrown if the liblzma call failed for some reason. You can find the liblzma documentation here:
<blockquote>
<p><code>&lt;code&gt;LZMA_MEMLIMIT_ERROR&lt;/code&gt;</code> No memory, or memory allocation limit was reached.
  This is not fatal, and the function may be called again to try
  compressing more data after freeing some memory, or moving the
  compression to a system with more memory available.</p>
</blockquote>
So the issue is that you're trying to compress too much data in one go. You could try to compress a smaller chunk at a time, or you could look into using <code>xz</code> instead, which is a command-line tool that can compress a stream.

