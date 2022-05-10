import select
+import pdb
+
+
+def test_memcached_server(test, name, default_port, default_host='127.0.0.1'):
+    port = os.getenv('MEMCACHED_PORT', default_port)
+    host = os.getenv('MEMCACHED_HOST', default_host)
+    test.globs['memcached'] = host + ':' + port
+
+
+def get_memcache_server(config):
+    return config.registry.memcached.items()[0][0]
+
+
+def get_memcache_client(config):
+    return config.registry.memcached.items()[0][1]
+
+
+def wait_for_memcache(host, port, ntries=100, interval=0.1):
+    # wait for memcache to start up
+    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    sock.settimeout(interval)
+
