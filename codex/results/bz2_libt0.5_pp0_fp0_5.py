import bz2
bz2.BZ2File(file_name, 'w')
# or
with bz2.BZ2File(file_name, 'w') as f:
    f.write(data)
</code>

