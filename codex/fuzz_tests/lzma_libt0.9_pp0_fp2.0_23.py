import lzma
lzma.open
</code>
There is no open function available.
I also tried <code>pip install python-lxml</code> but I am getting this error:
<code>error: command 'C:\\Program Files (x86)\\Microsoft Visual 
Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.20.27508\\bin\\HostX86\\x64\\cl.exe' failed with exit status 2</code>
Is there some way to install it?
Thank You


A:

Can you try this in a conda shell/window, if you are using anaconda:
<code>conda install -c anaconda lxml
</code>

