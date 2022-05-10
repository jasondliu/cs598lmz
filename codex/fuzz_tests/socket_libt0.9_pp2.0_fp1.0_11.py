import socket
+
+r = redis.Redis()
+
+def geolocate(host):
+    g = pygeoip.GeoIP('/usr/local/share/GeoIP/GeoLiteCity.dat')
+    return g.record_by_name(host)
+
+def main():
+    while True:
+        key, host, address = r.brpop('locator')
+        if len(address) > 0:
+            address = address.decode('ascii')
+            try:
+                record = geolocate(address)
+            except socket.gaierror, error:
+                print >> sys.stderr, "Problemas con %s: %s" % (address, unicode(error))
+                continue
+            if record is not None:
+                # save to cache
+                if 'country_code' not in record:
+                    record['country_code'] = ''
+                if 'city' not in record:
+                    record['city'] = ''
+                else:
+
