import socket
socket.if_indextoname(12)

`enp3s0`
## Which interfaces are up

`ip link show up`

Returns only the interfaces (not the output of the command)

## Useful commands

`ip link show <device>`

`ip addr show <device>`

## Test a connection

`ping <host>`

`ping -c 3 <host>`

`ping -D <host>`

`mtr -r <host>`
## Turn up a device

`ip link set <device> up`

## Turn down a device

`ip link set <device> down`

## Enable promiscuous mode 

`ip link set <device> promisc on`
## Disable promiscuous mode

`ip link set <device> promisc off`
## Set new MAC Address

`ip link set <device> address <mac_address>`

## Put an interface up

`ip link set <device> up`

*e.g.* `ip link set enp3s0 up`
## Put an interface down

`ip
