import socket
+from urllib.parse import urlparse
+
+from django.conf import settings
+from django.contrib.auth.models import User
+from django.contrib.sites.models import Site
+from django.core.urlresolvers import reverse
+from django.http import HttpResponseRedirect
+from django.test import TestCase
+from django.test.client import RequestFactory
+
+from allauth.account.forms import LoginForm
+from allauth.account.models import EmailAddress
+from allauth.account.utils import perform_login
+from allauth.socialaccount.models import SocialAccount
+
+from .. import views, models
+
+
+class BaseTest(TestCase):
+    def setUp(self):
+        self.user = User.objects.create_user(
+            username='user',
+            email='user@example.com',
+            password='password'
+        )
+        self.site = Site.objects.create(
+            name='example.com',
+            domain='example
