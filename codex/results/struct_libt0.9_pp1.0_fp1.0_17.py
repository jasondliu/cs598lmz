import _struct
+from scapy.fields import *
+from scapy.all import *
+from scapy.packet import *
+from scapy.plist import PacketList
+import socket
+import argparse
+from termcolor import colored
+from netifaces import interfaces, ifaddresses, AF_INET
+from time import sleep
+from subprocess import Popen, PIPE
+
+
+class SIP(Packet):
+    name = "SIP Packet"
+    fields_desc = [FieldLenField("Length", None, length_of="messageString"),
+                   StrLenField("messageString", "", length_from=lambda pkt: pkt.Length)]
+
+
+# Following function sends CS_NEW command to the control server.
+def connect_to_control_server(cont_server_ip, cont_server_port):
+    cs_new_msg = build_cs_new_command()
+    cont_server_response = send_msg_to_cont_server(cs_new_msg, cont_server_ip, cont_
