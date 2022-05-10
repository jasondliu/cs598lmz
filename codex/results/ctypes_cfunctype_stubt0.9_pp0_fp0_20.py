import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
</code>
And I tried to use <code>@register.function</code> to register this as a template function.
But I got this error:
<code>TemplateSyntaxError at /direct

Caught TypeError while rendering: object is not callable

Django Version: 1.8

Exception Type: TemplateSyntaxError

Exception Value:

Caught TypeError while rendering: object is not callable
</code>
In the logging I see:
<code>main.py", line 48, in &lt;module&gt; main() File ".myapp/main.py", line 44, in main django.setup() File "/home/xun/.env/lib/python2.7/site-packages/django/__init__.py", line 18, in setup apps.populate(settings.INSTALLED_APPS) File "/home/xun/.env/lib/python2.7/site-packages/django/apps/registry.py", line 85, in populate app_config = AppConfig.create(entry) File "/home/xun/.env/
