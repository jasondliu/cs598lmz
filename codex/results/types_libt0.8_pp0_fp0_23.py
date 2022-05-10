import types
types.MethodType.__init__(self, function, instance)

RuntimeError: maximum recursion depth exceeded while calling a Python object

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/var/www/html/wsgi.py", line 18, in &lt;module&gt;
    execute(['scrapy', 'crawl', 'my_spider', '-a', 'url=https://www.nairaland.com/'])
  File "/var/www/html/scrapy_app/scrapy_app/spiders/script.py", line 15, in execute
    execute(cmd, shell=True)
  File "/usr/local/lib/python2.7/subprocess.py", line 541, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['scrapy', 'crawl', 'my_spider', '-a', 'url=https://www.nairaland.com/']' returned non-zero exit status -
