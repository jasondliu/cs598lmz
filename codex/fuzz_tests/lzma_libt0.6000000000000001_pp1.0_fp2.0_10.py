import lzma
lzma.LZMAError

# This will show up in the traceback
raise lzma.LZMAError("This is an error message")
 
# This will not show up in the traceback
raise lzma.LZMAError("This is an error message") from None

# This will show up in the traceback
raise lzma.LZMAError("This is an error message") from KeyError("This is an error message")

# This will show up in the traceback
raise lzma.LZMAError("This is an error message") from KeyError("This is an error message") from None

# This will show up in the traceback
raise lzma.LZMAError("This is an error message") from None from None

# This will show up in the traceback
raise lzma.LZMAError("This is an error message") from KeyError("This is an error message") from KeyError("This is an error message")

# This will not show up in the traceback
raise lzma.LZMAError("This is an error message") from Key
