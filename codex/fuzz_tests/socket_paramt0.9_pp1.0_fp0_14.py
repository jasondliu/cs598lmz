import socket
socket.if_indextoname()

Get mac address of interface

Get it for connection

# TODO:
- factor out into utils file
- look at cleaning permissions issues on startup
  - e.g. `ip netns exec mynet ip link set ...`
- figure out how to get mac address of containers and renice them
- make sure it doesn't take over OS permissions
- find way to use /proc/net without root permissions
- look at /sys/class/net/enp3s0/
- look at /etc/network/interfaces.d/enp3s0
- listen for new interface events
- interface labels
  - can be found in ens33: operstate: "up"
- check out trafshow for bandwidth tracking
