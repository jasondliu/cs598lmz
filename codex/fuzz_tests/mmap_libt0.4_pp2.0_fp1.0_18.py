import mmap
import os

#
#   This is a Python implementation of the following C++ code:
#
#   #include <windows.h>
#   #include <stdio.h>
#
#   int main(int argc, char *argv[])
#   {
#       HANDLE file;
#       HANDLE map;
#       char *data;
#       DWORD size;
#
#       if (argc != 2)
#       {
#           printf("Usage: %s <file>\n", argv[0]);
#           return 1;
#       }
#
#       file = CreateFile(argv[1], GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, 0, NULL);
#       if (file == INVALID_HANDLE_VALUE)
#       {
#           printf("Cannot open file %s\n", argv[1]);
#           return 1;
#       }
#
#       size = GetFileSize(file, NULL);
#       if (size == 0)
