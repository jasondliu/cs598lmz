import socket
socket.if_indextoname(3)

# Import module
import subprocess
# Return output from the shell command
subprocess.check_output(["ls", "-l"])
# Run the command and store the results
returned_text = subprocess.check_output(["netstat", "-l"])
# Return text as a string
returned_text

# Import module
import re
# Return an iterator of all matching patterns
re.finditer(r"[0-9]+", "22 drummers, 11 pipers, 2 drummers, 1 pianist")
for match in re.finditer(r"[0-9]+", "22 drummers, 11 pipers, 2 drummers, 1 pianist"):
    match.group()

# Import module
import subprocess
import re
# Return output from the shell command
output = subprocess.check_output(["netstat", "-l"])
# Return text as a string
output = str(output)
# Return an iterator of all matching patterns
matches = re.finditer(r"[0-9]+", output)
for match in matches:
    match.group()

