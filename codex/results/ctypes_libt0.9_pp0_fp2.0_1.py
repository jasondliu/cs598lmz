import ctypes
ctypes.cdll.LoadLibrary("libelfin.dylib") 
elf_size = "/Users/joe/elfin_auth/start_end_elf.py"
 
py_compile.compile(elf_size)


size_data = ELF(ELFdirectory)
for key, value in size_data.section_size.items():
    if value > 0:
        print("Section_Size:", key, value)
        print ("---------------------------------------------------------------------------------------------------------------------")

print("Start_Address:",size_data.section_size.get("start_address"))
print ("---------------------------------------------------------------------------------------------------------------------")
print("End_Address:",size_data.section_size.get("end_address"))



# Print hexdump with size
size_data = ELF(ELFdirectory)
for key, value in size_data.size.items():
    if value > 0:
        print("Size:", key, value)

print ("---------------------------------------------------------------------------------------------------------------------")
for offset in range(0, size_data.size.get('headers'), 16):
    print( ' '.join( "%02X"
