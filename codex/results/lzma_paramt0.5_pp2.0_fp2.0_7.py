from lzma import LZMADecompressor
LZMADecompressor().decompress(open(infile, 'rb').read())
</code>
Or, if you don't have the <code>lzma</code> module, you can use <code>subprocess</code> to run the <code>xz</code> command line tool:
<code>import subprocess
subprocess.check_output(['xz', '--decompress', '--stdout', infile])
</code>

