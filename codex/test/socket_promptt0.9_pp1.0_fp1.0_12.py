import socket
# Test socket.if_indextoname (LP bug #1007581)

def get_default_iface():
  """Get the default interface on FreeBSD."""
  with open('/proc/net/route') as f:
    for line in f:
      fields = line.strip().split()
      if fields[1] != '00000000' or not int(fields[3], 16) & 2:
        continue
      return fields[0]


def main():
  assert socket.if_indextoname(1) == 'lo0'
  assert socket.if_indextoname(2) == get_default_iface()

if __name__ == '__main__':
  main()
