import select
# Test select.select
# Linux技术QQ群: 417802973 python
# https://github.com/pythonpeixun/article/issues/38
def test_select():
    infds, outfds, errfds = select.select([sys.stdin], [], [])
    if infds:
        fd = infds.pop()
        s = fd.read()
        if s in ("quit", "exit"):
            return
        print(s)
        test_select()


