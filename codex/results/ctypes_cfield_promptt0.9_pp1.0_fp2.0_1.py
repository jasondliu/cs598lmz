import ctypes
# Test ctypes.CField as CField
# This will fail in COMDAT cause ELF reserves table index
# 0 for GetBaseClassDescriptor, which is 8 bytes in size,
# While CField is 1 byte in size.

class TestCType(unittest.TestCase):
    def test(self):
        comdat = rctypesgen.gendll.test_ctypes_comdat.addresses[0]
        print(hex(comdat))
        asmcode = b"""
            movq 0x7f, %%rax
            movq 0x10, %%rbx
            andq %%rax, %%rbx
            orq %%rbx, %%rbx
            addq %%rbx, %%rbx
            movb %%bl, (%%rbx)
            ret
        """
        asmcode = asmcode.replace(b"\n", b"\r\n")
        interpreter = rctypesgen.gendll.test_ctypes_comdat.addresses[1]

        print("Writing code to {}".format(hex(comdat)))
        print(asmcode
