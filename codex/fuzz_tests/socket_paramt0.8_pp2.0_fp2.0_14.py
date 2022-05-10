import socket
socket.if_indextoname(1)

class networkInterfaceList:
    def __init__(self,name,ipaddr,macaddr,port,up,switch,arp_table_list,routing_table,ip_forwarding_list,dhcp_client_list,dhcp_server_list,dhcp_service_list,dhcp_status,dhcp_policy,proxy_arp):
        self.name = name
        self.ipaddr = ipaddr
        self.macaddr = macaddr
        self.port = port
        self.up = up
        self.switch = switch
        self.arp_table_list = arp_table_list
        self.routing_table = routing_table
        self.ip_forwarding_list = ip_forwarding_list
        self.dhcp_client_list = dhcp_client_list
        self.dhcp_server_list = dhcp_server_list
        self.dhcp_service_list = dhcp_service_list
        self.dhcp_status = dhcp_status
        self.dhcp_policy = dhcp_policy
       
