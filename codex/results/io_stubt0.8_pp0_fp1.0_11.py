import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

e = gdb.Breakpoint("test.c:85")

print view
</code>
When I run a regular program it works as expected, but when I use the script to run the same program I get:
<code>$ gdb -x script.py ./test
GNU gdb (GDB) Fedora (7.6.50.20130731-35.fc20)
Copyright (C) 2013 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later &lt;http://gnu.org/licenses/gpl.html&gt;
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
&lt;http://www.gnu.org/software/gdb/bugs/&gt;...
Reading symbols from /home/adam/test...done.
[New LWP 3237]


