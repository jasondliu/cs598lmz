from lzma import LZMADecompressor
LZMADecompressor().decompress(open('/proc/config.gz', 'rb').read())

# If you want to read the config from your own kernel, replace the path above with:
# /boot/config-`uname -r`

# This prints the config to standard out, which you can then redirect to a file:
# python3 extract_config.py &gt; my_config
</code>

