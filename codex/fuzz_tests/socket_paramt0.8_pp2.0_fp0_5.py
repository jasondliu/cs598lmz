import socket
socket.if_indextoname(socket.if_nametoindex('mon0'))

interface_name='mon0'
interface_mode=2
interface_channel='1'
interface_rate='6'
interface_mac='FF:FF:FF:FF:FF:FF'
track_bssid='FF:FF:FF:FF:FF:FF'
track_ssid='Au-Terrace'

mon=ManagedAP(interface_name,interface_mode,interface_channel,interface_rate,interface_mac)

mon.Start()
mon.Track(track_bssid,track_ssid)

while True:
    sleep(1)
