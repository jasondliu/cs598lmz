import _struct
+def pack_ip_addr(ip):
+    return _struct.pack('!L',ip)
+
+def unpack_ip_addr(buf):
+    return _struct.unpack('!L',buf)[0]
+
+def pack_mac_addr(mac):
+    assert len(mac) == 6
+    return _struct.pack('!6B',*mac)
+
+def unpack_mac_addr(buf):
+    assert len(buf) == 6
+    return _struct.unpack('!6B',buf)
+
+def pack_arp_header(arp_hdr):
+    return _struct.pack('!HHBBH6B4L',*arp_hdr)
+
+def unpack_arp_header(buf):
+    assert len(buf) == 28
+    return _struct.unpack('!HHBBH6B4L',buf)
+
+def pack_arp_packet(arp_hdr,arp_data):
+    return pack_arp_header(arp_hdr
