import mmap
import struct

class InvalidInputException(Exception):
  pass

ID_FIELD = "id"
STRING_FIELD = "string"
ENUM_FIELD = "enum"
SEX_FIELD = "sex"
UNUSED_FIELD = "UNUSED"
AGE_FIELD = "age"
EXTENSION_FIELD = "extension"

def sanitize_file(output_buffer, input_filename):
  with open(input_filename, "rb") as f:
    # memory-map the file, size 0 means whole file
    input_buffer = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    old_pos = 0
    output_buffer.write(input_buffer)

    while True:
      eol = input_buffer.find('\n', old_pos)
      if eol == -1:
        break

      in_line = input_buffer[old_pos:eol]
      old_pos = eol + 1

      tokens = in_line.split(',')

      if len(
