import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
which returns <code>b'\x01'</code>
I've been trying to implement this in Rust, but I don't know how to get the contents of the mmap after the file has been truncated. This is what I've tried:
<code>extern crate libc;
extern crate memmap;

use libc::{c_int, size_t};
use memmap::MmapMut;
use std::fs::OpenOptions;
use std::io::Write;

const O_TRUNC: c_int = 512;

fn main() {
    let mut file = OpenOptions::new()
        .write(true)
        .read(true)
        .create_new(true)
        .mode(0o666)
        .open("test")
        .unwrap();

    file.write_all(b"\x01").unwrap();
    let mut mmap = unsafe { MmapMut::map_mut(&amp;file).unwrap() };

    file.as_raw_
