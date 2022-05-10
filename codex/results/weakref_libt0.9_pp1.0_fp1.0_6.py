import weakref
+from flask import Flask
+from flaskext.celery import Celery
+from flaskext.testing import TestCase
+
+class FlaskCeleryCase(TestCase):
+
+    def create_app(self):
+        app = Flask(__name__)
+        app.config['CELERY_BROKER_URL'] = 'memory://'
+        app.config['CELERY_CACHE_BACKEND'] = 'memory://'
+        app.config['TESTING'] = True
+        celery = Celery(app)
+
+        @celery.task
+        def add(x, y):
+            return x + y
+
+        self.add = add
+        self.app = app
+        return app
+
+
+class TestCelery(FlaskCeleryCase):
+
+    def test_add(self):
+        result = self.add.delay(4, 4)
+        assert result.wait() == 8

