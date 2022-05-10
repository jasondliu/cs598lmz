import io
# Test io.RawIOBase
import io
fr = io.open("/etc/passwd", mode="rb")
six.assertCountEqual(self,
                     [x for x in fr],
                     [b'root:x:0:0:root:/root:/bin/bash\n',
                      b'bin:x:1:1:bin:/bin:/sbin/nologin\n',
                     ])


six.assertCountEqual(self,
                     (line for line in fr),
                     [b'root:x:0:0:root:/root:/bin/bash\n',
                      b'bin:x:1:1:bin:/bin:/sbin/nologin\n',
                     ])
six.assertCountEqual(self,
                     (line for line in fr),
                     [b'root:x:0:0:root:/root:/bin/bash\n',
                      b'bin:x:1:1:bin:/bin:/sbin/nologin\n',
                     ])
six.assertEqual(self,
                (list(fr)),
                [])
fr = io
