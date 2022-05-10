import _struct
import elf

class Exec(object):

    def __init__(self, filename):
        self.fd = open(filename, "r")
        self.header = elf.Elf32_Ehdr(self.fd.read(elf.sizeof(elf.Elf32_Ehdr)))
        if self.header.e_ident.ei_class:
            self.shtab_entry_size = elf.Elf64_Shdr.sizeof()
            self.shtab_entry_name = elf.Elf64_Shdr.name
        else:
            self.shtab_entry_size = elf.Elf32_Shdr.sizeof()
            self.shtab_entry_name = elf.Elf32_Shdr.name

        if self.header.e_ident.ei_class:
            self.phtab_size = elf.Elf64_Phdr.sizeof()
            self.phent_size = elf.Elf64_Phdr.sizeof()
            self.phnum = self.header.e_phnum
        else:
            self.phtab_size = elf.
