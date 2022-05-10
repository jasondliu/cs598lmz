import socket
+import struct
+
+
+def get_local_ip():
+    """ Get the local ip address of the machine. """
+    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+    s.connect(('8.8.8.8', 0))
+    local_ip_address = s.getsockname()[0]
+    s.close()
+    return local_ip_address
+
+
+def get_remote_ip(host):
+    """ Get the ip address of a host. """
+    return socket.gethostbyname(host)
+
+
+def get_mac(ip_address):
+    """ Get the mac address of a host. """
+    # Create a raw socket and bind it to the public interface
+    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+    s.bind(('', 0))
+    # Set the ARP request parameters
+    arp_request = struct.pack('!2s2s
