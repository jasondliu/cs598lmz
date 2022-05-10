import _struct

class TestCoroutine(asyncio.coroutine):
    def test(self):
        print('test')



@asyncio.coroutine
def hello():
    print('Hello World!')
    r = yield from asyncio.sleep(1)
    print('Hello Again!')
    return r

@asyncio.coroutine
def hello_world():
    yield from hello()
    print('Hello World!')

@asyncio.coroutine
def test_create(a,b):
    print('test_{}_{}', a, b)
    return a + b

@asyncio.coroutine
def wget(host):
    print('wget {} ...'.format(host))
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while
