import socket
+
+import requests
+from lxml import html
+
+from utils import is_valid
+
+
+def test_get_sites():
+    resp = requests.get('http://localhost:3000')
+    root = html.fromstring(resp.content)
+
+    assert len(root.cssselect('#sites tbody tr')) == 4
+
+
+def test_add_site():
+    url1 = 'http://localhost:3000/'
+    url2 = 'http://www.cargurus.com'
+    res_code = requests.post(
+        url1,
+        data={
+            'url': url2,
+            'interval': 180
+        }
+    ).status_code
+    assert res_code == 201
+    test_site = Site.objects.get(url=url2)
+    assert test_site.interval == 180
+
+
+def test_add_site_fail():
+    url1 = 'http://localhost:3000/'
+    url2
