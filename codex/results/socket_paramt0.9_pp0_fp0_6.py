import socket
socket.if_indextoname(iface.index)
EOM
	done
	for iface in "${ENCRYPTED_IFACES[@]}"; do
		iface=$(netctl list | grep '*' | sed -e 's/.*\(eno1\).*/\1/')
		sudo systemd-networkd-wait-online --interface=$iface --timeout=1 -q
		sudo ip a add 10.132.0.2/30 dev ${iface} 
		ssh::keygen
		ssh::copykey
	done
}

function main(){
	if [ -z "$ACTION" ]; then
		echo "Need an action. Use --help"
		exit 1
	else
		$ACTION 
	fi
}

main
