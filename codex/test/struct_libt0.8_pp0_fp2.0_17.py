import _struct
import _shutil

# The hexadecimal structure of a PE file is as follows:
# Offset	Size	Description
# 0			Magic number									The number "P" followed by the number "E". (4 bytes)
# 4			Machine											The type of machine on which the image is to be run. (2 bytes)
# 6			NumberOfSections								The number of sections in the image. (2 bytes)
# 8			TimeDateStamp									The date and time at which the image was created. (4 bytes)
# 12		PointerToSymbolTable							The address of the symbol table, relative to the image base. (4 bytes)
# 16		NumberOfSymbols									The number of symbols in the symbol table. (4 bytes)
# 20		SizeOfOptionalHeader							The number of bytes in the optional header.
