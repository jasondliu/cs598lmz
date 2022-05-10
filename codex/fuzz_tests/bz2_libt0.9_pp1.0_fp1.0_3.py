import bz2
bz2_output = bz2.BZ2File('/tmp/names.cbz', 'wb')
with open('/tmp/names.csv', 'rb') as f:
    for line in f:
        bz2_output.write(line)
bz2_output.close()
%%bash
file /tmp/names.csv /tmp/names.cbz

ls -lh /tmp/names.csv /tmp/names.cbz

bzip2 -d -k /tmp/names.cbz

file /tmp/names.cbz.out

rm -f /tmp/names.cbz.out

!head -n 5 /tmp/names.csv
!echo ''
!head -n 5 /tmp/names.cbz

# NOTE: it is possible to zip or bzip2 or gzip or whatever to a ready-to-use file!
with bz2.open('/tmp/names.bz2', 'wb') as fout:
    with open('/tmp/names.csv', 'rb') as fin:
        fout.write(fin
