from lzma import LZMADecompressor
LZMADecompressor.__init__.__defaults__ = (False, None, 1)

from lzma import open as lzma_open
lzma_open.__defaults__ = (None, None, None, None, None, None)

# imghdr
import imghdr
imghdr.tests.__defaults__ = ()

# smb/base.py
import smb as smb_module
smb_module.base.__defaults__ = (None,)

# smb/__init__.py
import smb as smb_module
smb_module.__init__.__defaults__ = (None,)

# smb/tree.py
import smb as smb_module
smb_module.tree.__init__.__defaults__ = (None,)

# smb/base.py
import smb as smb_module
smb_module.base.__init__.__defaults__ = (None,)

# smb/base.py
import smb as smb_module
smb_module.base.__init
