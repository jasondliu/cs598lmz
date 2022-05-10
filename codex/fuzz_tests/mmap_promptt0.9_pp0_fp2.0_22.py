import mmap
# Test mmap.mmap.write()

with open(__file__, 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'Written')
    print(m[0:len('Written')])
    m.close()

with open(__file__, 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'Written again')
    print(m[0:len('Written again')])
EOF

run_python_until_end "$content"
