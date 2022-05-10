import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)

# SELECT - SELECT -> WSAAsyncSelect
# (event, haskell) -&gt; callback -&gt; non-blocking IO
</code>
You can read more about the MFC-Event-driven programming model in the MSDN article "Synchronizing Threads with Messages".

