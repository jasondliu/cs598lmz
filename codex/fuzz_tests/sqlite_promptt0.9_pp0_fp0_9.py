import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("app.db")
import uuid
import os

# Assign values to r/w and execute permissions
S_IRWXU = octal_permissions("700")
S_IRUSR = octal_permissions("400")
S_IWUSR = octal_permissions("200")
S_IXUSR = octal_permissions("100")
S_IRWXG = octal_permissions("070")
S_IRGRP = octal_permissions("040")
S_IWGRP = octal_permissions("020")
S_IXGRP = octal_permissions("010")
S_IRWXO = octal_permissions("007")
S_IROTH = octal_permissions("004")
S_IWOTH = octal_permissions("002")
S_IXOTH = octal_permissions("001")

# Setting up our number for the permissions (octal)
def octal_permissions(octal_permissions):
    return int(octal_permissions, base=8)

#Get
