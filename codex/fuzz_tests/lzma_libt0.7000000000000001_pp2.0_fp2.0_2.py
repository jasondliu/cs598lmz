import lzma
lzma.LZMAError: Initializing LZMA decoder failed
</code>
I am trying to install the packages on my Raspberry Pi. I have Python 3.5.2 installed.
I tried to install lzma but it seems I already have it installed.
<code>pi@raspberrypi:~ $ python -m pip install lzma
Collecting lzma
  Using cached lzma-0.0.9.tar.bz2
Requirement already satisfied: setuptools in /usr/local/lib/python3.5/dist-packages (from lzma)
Building wheels for collected packages: lzma
  Running setup.py bdist_wheel for lzma
  Running command /usr/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-l2f_jq_3/lzma/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(
