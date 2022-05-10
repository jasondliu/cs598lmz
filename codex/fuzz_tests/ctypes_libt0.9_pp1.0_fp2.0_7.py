import ctypes
ctypes.CDLL("libc.so.6")(setresuid = None)

IP = ""
PORT = ""

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

my_conn = ssh_client.connect(IP, port=PORT, username="user", password=Password)
chan = my_conn.invoke_shell()

output = chan.recv(2048)
print(output.decode())

chan.send("whoami > whoami.txt\n")


########## check if user is root by reading contents of whoami.txt ###########

with open('whoami.txt', 'r') as file:
    data = file.read()

if data == 'root\n':
    print("YOU ARE ROOT!!! :)")
else:
    print("YOU ARE NOT ROOT!!! :(")
