import lzma
lzma.compress('/home/myuser/mydata.csv') # This will return the compressed data as bytes.
</code>
Compression using lzma is slower than using gzip, but the resulting file size is much smaller:
<code>$ ls -lh mydata.csv
19M mydata.csv
$ gzip mydata.csv
$ ls -lh mydata.csv.gz
8.2M mydata.csv.gz
$ lzma mydata.csv
$ ls -lh mydata.csv.lzma
252K mydata.csv.lzma
</code>
I think lzma compression is enabled by default in gzip compression. So it should get the best of both worlds (speed + compression). You can try bcgzip.
<code>$ bcgzip -vd mydata.csv.gz
</code>

If you want to compress a database, you can use mysql/maria-db dump.
<code>mysqldump -u root -p your_db &gt; database.sql                              # First, dump your database with mysqldump
