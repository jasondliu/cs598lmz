import socket
socket.if_indextoname(3)

#3. Assign ITP1_12.py and ITP1_14.py to args['wsgi.file_wrapper'].read()
env['wsgi.file_wrapper'] = open('ITP1_11_B.py')
# os.system('ls')bashでやること
# subprocess.call(['ls'])
# os.system('wc -l'+' ITP1_9_B.py')
# os.system('ls | wc -l')
