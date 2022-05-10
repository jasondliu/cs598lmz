import lzma
lzma.LZMAError: Input format not supported by decoder
</code>
I have the following installed
<code>$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.6 LTS
Release:        16.04
Codename:       xenial
$ python --version
Python 3.7.3
$ pip3 list
Package    Version
---------- -------
pip        19.3.1
setuptools 41.6.0
$ pip3 install lzma
Requirement already satisfied: lzma in /usr/local/lib/python3.7/dist-packages (0.0.8)
</code>
Any idea how to fix this? Thanks


A:

The problem is that the <code>lzma</code> module is a very thin wrapper around the liblzma library.  This library is not installed by default on Ubuntu (and probably on other linux distros too).
To install the library on Ubuntu, run:
<code>sudo apt install liblzma-dev
</code>
If you
