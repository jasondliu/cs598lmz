import lzma
lzma.decompress(open(sys.argv[1],'rb').read())
```

We can now see the file that is being written to `/tmp/file`.
```
$ python test.py test.lzma
$ cat /tmp/file
{ "foo": "bar" }
```

## Solution

Now we need to use the same methods to extract the secret in `./data`.

```
$ python test.py data
$ cat /tmp/file
{ "secret": "ZmxhZ3twMDFfTm93X2l0c19kYXJrX3RoaW5raW5nfQ=="}
```

Decoding from base64 and we get the flag.

```
$ echo ZmxhZ3twMDFfTm93X2l0c19kYXJrX3RoaW5raW5nfQ== | base64 --decode
flag{p01_Now_its_dark_thinking}
```

Flag: `flag{p01_Now_its_dark_
