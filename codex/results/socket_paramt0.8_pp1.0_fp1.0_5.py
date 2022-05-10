import socket
socket.if_indextoname(socket.iff_index(if_name_check))

#subprocess.run('sudo sysctl -w net.ipv6.conf.all.forwarding=1', shell=True)

# call the class
cli = Cli(ifname=if_name)

# start cli
cli.cmdloop()
