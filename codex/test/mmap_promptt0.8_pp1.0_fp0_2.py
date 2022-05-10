import mmap
# Test mmap.mmap.write(bytearray(b'\xC2\x0C\x00\x00'))

# Test running a C program from Python
# import subprocess
# subprocess.call("./test_C")

# Test running a for-loop in a subprocess
# for i in range(10):
#     print(process_command('ls'))

# Test subprocess.Popen with stdout
"""
p = subprocess.Popen(['../C_code/a.out'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    # print(line)
"""

# Test subprocess.Popen with string value (stdout)
"""
p = subprocess.Popen(['../C_code/a.out'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
line = p.stdout.readline().decode('utf-8')
print(line)
print(line == 'Error: 0')
"""

