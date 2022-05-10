import sys, threading
threading.Thread(target=lambda:list(map(sys.stdout.buffer.write, iter(sys.stdin.buffer.read, b'')))).start()

```

```
#!/usr/bin/env perl

my $data;
while (<STDIN>) {
    $data .= $_;
}
print $data
```

```
#!/usr/bin/perl

use strict;
use warnings FATAL => 'all';

# Read from STDIN
my $data = do { local $/; <STDIN> };
print $data
```

```
#!/usr/bin/env bash

while read -r; do
  echo "$REPLY"
done
```
