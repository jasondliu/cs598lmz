fn = lambda: None
# Test fn.__code__.co_filename fails with "Not supported"
if sys.platform == "cli":
    setattr(fn, "__code__", NotImplemented)
else:
    setattr(fn, "func_code", NotImplemented)

#print(sys.getfilesystemencoding())   # <-- 'utf-8'
#print(os.fsencode(fn.__code__.co_filename))    # <-- b'c:\\python\\lib\\__main__.py'
try:
    #print(os.fsencode(fn.func_code.co_filename))    # <-- b'c:\\python\\lib\\__main__.py'
    pass
except Exception:
    pass
#print(os.fsdecode(os.fsencode(fn.__code__.co_filename)))   # <-- 'c:\\python\\lib\\__main__.py'
#print(os.fsdecode(os.fsencode(fn.__code__.co_filename)).encode('mbcs'))    # <-- b'c:\
