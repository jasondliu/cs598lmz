import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
after i run this code, in the fd, the file_ops is nil, there is no way to call a->read. so i modify file_ops to a, and then it can run.
i add this code:
<code>f.seek(0, os.SEEK_SET)
f.read()
</code>
after truncate, there is no crash.
i use gdb to check the fd, there is no crash.
<code>Program received signal SIGSEGV, Segmentation fault.
0x000000005ef5b5aa in mmap_fault () from /usr/lib/x86_64-linux-gnu/libsystemd-shared-231.so
Missing separate debuginfos, use: debuginfo-install GConf2-2.64.4-4.fc25.x86_64 dbus-glib-0.108-10.fc25.x86_64 dbus-libs-1.10.20-1.fc25.x86_64 e2fsprogs-1.43.4-6.fc
