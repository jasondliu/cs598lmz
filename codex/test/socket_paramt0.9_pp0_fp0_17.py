import socket
socket.if_indextoname(3) # will get ens3

1+10000

-1%2

string = " hello world "
dir(string)

"hello world".upper().strip().endswith("d")

string.startswith("hello")

string.strip()

string.endswith("d")

string.replace("hello", "Hi")

ip = "1234.43.123.11"
print(ip.split('.'))

ip_splited = ip.split('.')
ip_splited[1]

ip_reassembled = '.'.join(ip_splited)

is_ip_splited_invalid = ip_splited.__contains__('..') # contains is not working

print(is_ip_splited_invalid)

ip_reassembled.split('.')

ip = "192.168.1.1"

"\n".join(ip.split('.'))

"hello world".upper()
"hello world".lower()
"   hello world".strip()

