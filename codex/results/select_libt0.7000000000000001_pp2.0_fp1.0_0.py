import select
import paramiko
import time
import subprocess
import sys
import getpass

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip = raw_input("Enter ip address: ")
username = raw_input("Enter username: ")

password = getpass.getpass("Enter password: ")

ssh.connect(ip, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command("show run")

output = stdout.readlines()

for line in output:
    print line

ssh.close()
