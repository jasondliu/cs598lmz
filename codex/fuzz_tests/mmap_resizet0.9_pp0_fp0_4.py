import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # TypeError
    f.close()
    assert a == b''
</code>
Test with mmap.close()
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    try:
        m[:]  # error with mmap.mmap.error
    except mmap.error as e:
        assert False
    except IndexError as e:
        assert True
    finally:
        f.close()
</code>

