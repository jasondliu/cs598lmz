import lzma
lzma.decompress("XZ")
</code>
This will throw an error:
<code>&gt;&gt;&gt; import lzma
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/lib/python3.5/lzma.py", line 47, in &lt;module&gt;
    _lzma.error: Failed to initialize the back-end library. Possible causes:
    * Incorrect build options for liblzma; recompile from source with correct
      options.
    * In combination with operating systems that have case-insensitive or case-
      converting file systems, a file that has the same name as any module in
      this package except for the letter case, for example "lzma.py"
    * Corrupt installation of this package; try reinstalling it with:
      $ sudo apt install --reinstall python3-pyliblzma
</code>
I've tried using <code>sudo apt install --reinstall python3-
