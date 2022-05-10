import lzma
lzma.LZMAError: Cannot allocate memory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/bin/pip", line 11, in &lt;module&gt;
    load_entry_point('pip==19.0.3', 'console_scripts', 'pip')()
  File "/usr/local/lib/python3.7/site-packages/pkg_resources/__init__.py", line 489, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
  File "/usr/local/lib/python3.7/site-packages/pkg_resources/__init__.py", line 2852, in load_entry_point
    return ep.load()
  File "/usr/local/lib/python3.7/site-packages/pkg_resources/__init__.py", line 2443, in load
    return self.resolve()
  File "/usr/local/lib/python3.7/site-packages/pkg_resources
